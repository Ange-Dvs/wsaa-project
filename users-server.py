from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_url_path='', static_folder='.')
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

from usersDAO import usersDAO

@app.route('/')
@cross_origin()
def index():
    return app.send_static_file('usersviewer.html')

#curl "http://127.0.0.1:5000/users"
@app.route('/users')
@cross_origin()
def getAll():
    #print("in getall")
    results = usersDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/users/2"
@app.route('/users/<int:id>')
@cross_origin()
def findById(id):
    foundUser = usersDAO.findByID(id)
    return jsonify(foundUser)

#curl  -i -H "Content-Type:application/json" -X POST -d "#{\"title\":\"hello\",\"author\":\"someone\","price\":123}" http://127.#0.0.1:5000/users
@app.route('/users', methods=['POST'])
@cross_origin()
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    user = {
        "firstName": request.json['firstName'],
        "lastName": request.json['lastName'],
        "age": request.json['age'],
        "goal": request.json['goal'],
        "startingWeight": request.json['startingWeight'],
        "currentWeight": request.json['currentWeight'],
    }
    addeduser = usersDAO.create(user)
    
    return jsonify(addeduser)

#curl  -i -H "Content-Type:application/json" -X PUT -d "#{\"title\":\"hello\",\"author\":\"someone\","price\":123}" http://127.#0.0.1:5000/users/1
@app.route('/users/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    foundUser = usersDAO.findByID(id)
    if not foundUser:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)

    if 'firstName' in reqJson:
        foundUser['firstName'] = reqJson['firstName']
    if 'lastName' in reqJson:
        foundUser['lastName'] = reqJson['lastName']
    if 'age' in reqJson:
        foundUser['age'] = reqJson['age']
    if 'goal' in reqJson:
        foundUser['goal'] = reqJson['goal']
    if 'startingWeight' in reqJson:
        foundUser['startingWeight'] = reqJson['startingWeight']
    if 'currentWeight' in reqJson:
        foundUser['currentWeight'] = reqJson['currentWeight']
    usersDAO.update(id,foundUser)
    return jsonify(foundUser)

@app.route('/users/<int:id>' , methods=['DELETE'])
@cross_origin()
def delete(id):
    try:
        usersDAO.delete(id)
        return jsonify({"done":True})
    except Exception as e:
        print("Error deleting user:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__' :
    app.run(debug= True)
