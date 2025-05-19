from flask import Flask, jsonify, request, abort, send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_url_path='', static_folder='.')
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

from dao.usersDAO import usersDAO
from dao.workoutsDAO import workoutsDAO 
from dao.weightDAO import weightDAO

# Calls for HTML pages
@app.route('/')
def home():
    return send_from_directory('html', 'index.html')

@app.route('/users')
@cross_origin()
def users():
    return send_from_directory('html', 'usersviewer.html')

@app.route('/workouts')
@cross_origin()
def workouts():
    return send_from_directory('html', 'workoutsviewer.html')

@app.route('/weight-management')
@cross_origin()
def weight_view():
    return send_from_directory('html', 'weightviewer.html')

# Calls for getting information for users
@app.route('/api/users')
@cross_origin()
def getAllUsers():
    results = usersDAO.getAllUsers()
    return jsonify(results)

@app.route('/api/users/<int:userID>', methods=['GET'])
@cross_origin()
def findById(userID):
    foundUser = usersDAO.findByID(userID)
    return jsonify(foundUser)

@app.route('/api/users', methods=['POST'])
@cross_origin()
def createUser():
    
    if not request.json:
        abort(400)
    user = {
        "firstName": request.json['firstName'],
        "lastName": request.json['lastName'],
        "age": request.json['age'],
        "goal": request.json['goal'],
        "startingBodyWeight": request.json['startingBodyWeight'],
        "currentBodyWeight": request.json['currentBodyWeight'],
    }
    addeduser = usersDAO.createUser(user)
    
    return jsonify(addeduser)

@app.route('/api/users/<int:userID>', methods=['PUT'])
@cross_origin()
def update(userID):
    foundUser = usersDAO.findByID(userID)
    if not foundUser:
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'age' in reqJson and type(reqJson['age']) is not int:
        abort(400, description = "Age must be a whole number")
    if 'startingBodyWeight' in reqJson:
        try:
            float(reqJson['startingBodyWeight'])
        except (ValueError, TypeError):
            abort(400, description="startingBodyWeight must be a number")
    if 'currentBodyWeight' in reqJson:
        try:
            float(reqJson['currentBodyWeight'])
        except (ValueError, TypeError):
            abort(400, description="currentBodyWeight must be a number")

    if 'firstName' in reqJson:
        foundUser['firstName'] = reqJson['firstName']
    if 'lastName' in reqJson:
        foundUser['lastName'] = reqJson['lastName']
    if 'age' in reqJson:
        foundUser['age'] = reqJson['age']
    if 'goal' in reqJson:
        foundUser['goal'] = reqJson['goal']
    if 'startingBodyWeight' in reqJson:
        foundUser['startingBodyWeight'] = reqJson['startingBodyWeight']
    if 'currentBodyWeight' in reqJson:
        foundUser['currentBodyWeight'] = reqJson['currentBodyWeight']
    usersDAO.update(userID,foundUser)
    return jsonify(foundUser)

@app.route('/api/users/<int:userID>' , methods=['DELETE'])
@cross_origin()
def delete(userID):
    try:
        usersDAO.delete(userID)
        return jsonify({"done":True})
    except Exception as e:
        print("Error deleting user:", e)
        return jsonify({"error": str(e)}), 500

# Calls for getting information for workouts 
@app.route('/api/workouts', methods=['GET'])
@cross_origin()
def getAllWorkouts():
    results = workoutsDAO.getAllWorkouts()
    return jsonify(results)

@app.route('/api/workouts/<int:workoutID>', methods=['GET'])
@cross_origin()
def getWorkoutByID(workoutID):
    workout = workoutsDAO.findWorkoutByID(workoutID)
    return jsonify(workout)

@app.route('/api/workouts', methods=['POST'])
@cross_origin()
def createWorkout():
    if not request.json:
        abort(400)

    workout = {
        "userID": request.json["userID"],
        "sessionType": request.json["sessionType"],
        "location": request.json["location"],
        "durationMinutes": request.json["durationMinutes"],
        "difficulty": request.json["difficulty"],
        "rating": request.json["rating"]
    }

    addedWorkout = workoutsDAO.createWorkout(workout)
    return jsonify(addedWorkout), 201

@app.route('/api/workouts/<int:workoutID>', methods=['PUT'])
@cross_origin()
def updateWorkout(workoutID):
    existingWorkout = workoutsDAO.findWorkoutByID(workoutID)
    if not existingWorkout:
        abort(404)
    
    if not request.json:
        abort(400)
    
    reqJson = request.json
    if 'rating' in reqJson and not (1 <= int(reqJson['rating']) <= 5):
        abort(400, description="Rating must be between 1 and 5")

    for field in ['userID', 'sessionType', 'location', 'durationMinutes', 'difficulty', 'rating']:
        if field in reqJson:
            existingWorkout[field] = reqJson[field]
    
    workoutsDAO.updateWorkout(workoutID, existingWorkout)
    return jsonify(existingWorkout)

@app.route('/api/workouts/<int:workoutID>', methods=['DELETE'])
@cross_origin()
def deleteWorkout(workoutID):
    try:
        workoutsDAO.deleteWorkout(workoutID)
        return jsonify({"done": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Calls for getting information for weight-management
@app.route('/api/weight-management', methods=['GET'])
@cross_origin()
def getWeightLogs():
    return jsonify(weightDAO.getAllWeights())

@app.route('/api/weight-management', methods=['POST'])
@cross_origin()
def createWeightLog():
    data = request.get_json()
    return jsonify(weightDAO.createWeightEntry(data))

@app.route('/api/weight-management/<int:id>', methods=['DELETE'])
@cross_origin()
def deleteWeightLog(id):
    weightDAO.deleteWeightEntry(id)
    return jsonify({"message": f"Weight entry {id} deleted"})

@app.route('/api/weight-management/<int:id>', methods=['PUT'])
@cross_origin()
def updateWeightLog(id):
    data = request.get_json()
    weightDAO.updateWeightEntry(id, data)
    return jsonify({"message": f"Weight entry {id} updated"})

# Calls for getting information for summary data on homepage
@app.route("/api/dashboard-data", methods=["GET"])
def dashboard_data():
    cursor = workoutsDAO.getcursor()  
    cursor.execute("SELECT DATABASE();")
    print("Currently connected to DB:", cursor.fetchone())
    
    stats = workoutsDAO.get_dashboard_stats()
    return jsonify(stats)

@app.route("/api/user-summary", methods=["GET"])
def user_summary():
    stats = usersDAO.get_user_stats()
    return jsonify(stats)


if __name__ == '__main__' :
    app.run(debug= True)
