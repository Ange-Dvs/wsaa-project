# workoutsDAO.py
# Provides database operations related to logged workout sessions.
# Author: Angela Davis

import mysql.connector
import dbconfig as cfg
import datetime

class WorkoutsDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        # Loading database credentials from config file
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self, dictionary=False): 
        # Establishing the connection and returning the cursor
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor(dictionary=dictionary)
        return self.cursor

    def closeAll(self):
        # Closing the database connection
        self.connection.close()
        self.cursor.close()
         
    def getAllWorkouts(self):
        # Getting all workouts and converting to a list of dictionaries
        cursor = self.getcursor()
        sql="select * from workouts ORDER BY workout_date DESC"
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
        # Fetching a workout entry by the workout ID entered
        cursor = self.getcursor()
        sql="select * from workouts where workoutID = %s"
        values = (workoutID,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def createWorkout(self, workout):
        # Adding a new user
        cursor = self.getcursor()
        sql="""
            INSERT INTO workouts 
            (workout_date, userID, sessionType, location, durationMinutes, difficulty, rating) 
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
        values = (
            workout.get("workout_date"),
            workout.get("userID"),
            workout.get("sessionType"),
            workout.get("location"),
            workout.get("durationMinutes"),
            workout.get("difficulty"),
            workout.get("rating")
        )
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        workout["workoutID"] = newid
        self.closeAll()
        return workout


    def updateWorkout(self, workoutID, workout):
        # Updating the information for a workout entry
        cursor = self.getcursor()
        sql = """
            UPDATE workouts 
            SET workout_date=%s, userID=%s, sessionType=%s, location=%s, 
                durationMinutes=%s,difficulty=%s, rating=%s 
            WHERE workoutID = %s
        """
        print(f"update users {workout}")
        values = (
            workout.get("workout_date"),
            workout.get("userID"),
            workout.get("sessionType"),
            workout.get("location"),
            workout.get("durationMinutes"),
            workout.get("difficulty"),
            workout.get("rating"),
            workoutID
        )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def deleteWorkout(self, workoutID):
        # Deleting a workout entry using the workout ID
        cursor = self.getcursor()
        sql="delete from workouts where workoutID = %s"
        values = (workoutID,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        print("delete done")

    def convertToDictionary(self, resultLine):
        # Converting results to dictionary
        attkeys = ['workoutID', 'workout_date', 'userID', 'sessionType', 'location', 'durationMinutes', 'difficulty', 'rating']
        workout = {}
        for i, attrib in enumerate(resultLine):
            key = attkeys[i]
            if key == "workout_date" and isinstance(attrib, (datetime.date, datetime.datetime)):
                workout[key] = attrib.strftime('%Y-%m-%d')
            else:
                workout[key] = attrib
        return workout

    def get_dashboard_stats(self):
        # Returning summary statistics for workouts table and top 3 session types
        cursor = self.getcursor(dictionary=True)
        
        # Get summary stats
        sql_summary = """
            SELECT 
                COUNT(*) AS total_workouts,
                ROUND(AVG(durationMinutes)) AS avg_duration,
                COUNT(DISTINCT userID) AS unique_users
            FROM workouts;
        """
        cursor.execute(sql_summary)
        summary = cursor.fetchone()

        # Get top 3 session types
        sql_top_types = """
            SELECT sessionType
            FROM workouts
            GROUP BY sessionType
            ORDER BY COUNT(*) DESC
            LIMIT 3;
        """
        cursor.execute(sql_top_types)
        top_types = [row["sessionType"] for row in cursor.fetchall()]

        self.closeAll()

        # Combine all results
        return {
            "total_workouts": summary["total_workouts"],
            "avg_duration": summary["avg_duration"],
            "unique_users": summary["unique_users"],
            "top_session_types": top_types
        }
        
workoutsDAO = WorkoutsDAO()