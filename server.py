from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_url_path='', static_folder='.')
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

from usersDAO import usersDAO
from workoutsDAO import workoutsDAO 

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/users')
@cross_origin()
def users():
    return app.send_static_file('usersviewer.html')

@app.route('/workouts')
@cross_origin()
def workouts():
    return app.send_static_file('workoutsviewer.html')

#curl "http://127.0.0.1:5000/users"
@app.route('/api/users')
@cross_origin()
def getAllUsers():
    #print("in getall")
    results = usersDAO.getAllUsers()
    return jsonify(results)

#curl "http://127.0.0.1:5000/users/2"
@app.route('/users/<int:userID>')
@cross_origin()
def findById(userID):
    foundUser = usersDAO.findByID(userID)
    return jsonify(foundUser)

#curl  -i -H "Content-Type:application/json" -X POST -d "#{\"title\":\"hello\",\"author\":\"someone\","price\":123}" http://127.#0.0.1:5000/users
@app.route('/users', methods=['POST'])
@cross_origin()
def createUser():
    
    if not request.json:
        abort(400)
    # other checking 
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

#curl  -i -H "Content-Type:application/json" -X PUT -d "#{\"title\":\"hello\",\"author\":\"someone\","price\":123}" http://127.#0.0.1:5000/users/1
@app.route('/users/<int:userID>', methods=['PUT'])
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

@app.route('/users/<int:userID>' , methods=['DELETE'])
@cross_origin()
def delete(userID):
    try:
        usersDAO.delete(userID)
        return jsonify({"done":True})
    except Exception as e:
        print("Error deleting user:", e)
        return jsonify({"error": str(e)}), 500

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



if __name__ == '__main__' :
    app.run(debug= True)
