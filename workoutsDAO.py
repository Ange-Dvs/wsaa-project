# workout dao 
# this is a demonstration a data layer that connects to a datbase
# Author: Angela Davis

import mysql.connector
import dbconfig as cfg
class WorkoutsDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def getAllWorkouts(self):
        cursor = self.getcursor()
        sql="select * from workouts"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findWorkoutByID(self, workoutID):
        cursor = self.getcursor()
        sql="select * from workouts where workoutID = %s"
        values = (workoutID,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def createWorkout(self, workout):
        cursor = self.getcursor()
        sql="insert into workouts (userID, sessionType, location, durationMinutes, difficulty, rating) values (%s,%s,%s,%s,%s,%s)"
        values = (workout.get("userID"), workout.get("sessionType"), workout.get("location"), workout.get("durationMinutes"), workout.get("difficulty"), workout.get("rating"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        workout["workoutID"] = newid
        self.closeAll()
        return workout


    def updateWorkout(self, workoutID, workout):
        cursor = self.getcursor()
        sql="update workouts set userID=%s, sessionType=%s, location=%s, durationMinutes=%s, difficulty=%s, rating=%s where workoutID = %s"
        print(f"update users {workout}")
        values = (workout.get("userID"), workout.get("sessionType"), workout.get("location"), workout.get("durationMinutes"), workout.get("difficulty"), workout.get("rating"), workoutID)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def deleteWorkout(self, workoutID):
        cursor = self.getcursor()
        sql="delete from workouts where workoutID = %s"
        values = (workoutID,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

    def convertToDictionary(self, resultLine):
        attkeys=['workoutID','userID','sessionType', 'location', 'durationMinutes', 'difficulty', 'rating']
        workout = {}
        currentkey = 0
        for attrib in resultLine:
            workout[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return workout

        
workoutsDAO = WorkoutsDAO()