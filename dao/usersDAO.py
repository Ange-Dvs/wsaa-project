#
# this is a demonstration a data layer that connects to a datbase
# Author: Andrew Beatty

import mysql.connector
import dbconfig as cfg
class UsersDAO:
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

    def getcursor(self, dictionary=False): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor(dictionary=dictionary)
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def getAllUsers(self):
        cursor = self.getcursor()
        sql="select * from users"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, userID):
        cursor = self.getcursor()
        sql="select * from users where userID = %s"
        values = (userID,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def createUser(self, user):
        cursor = self.getcursor()
        sql="insert into users (firstName, lastName, age, goal, startingBodyWeight, currentBodyWeight) values (%s,%s,%s,%s,%s,%s)"
        values = (user.get("firstName"), user.get("lastName"), user.get("age"), user.get("goal"), user.get("startingBodyWeight"), user.get("currentBodyWeight"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        user["userID"] = newid
        self.closeAll()
        return user


    def update(self, userID, user):
        cursor = self.getcursor()
        sql="update users set firstName= %s,lastName=%s, age=%s, goal=%s, startingBodyWeight=%s, currentBodyWeight=%s  where userID = %s"
        print(f"update users {user}")
        values = (user.get("firstName"), user.get("lastName"), user.get("age"), user.get("goal"), user.get("startingBodyWeight"), user.get("currentBodyWeight"), userID)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, userID):
        cursor = self.getcursor()
        sql="delete from users where userID = %s"
        values = (userID,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

    def convertToDictionary(self, resultLine):
        attkeys=['userID','firstName','lastName', 'age', 'goal', 'startingBodyWeight', 'currentBodyWeight']
        user = {}
        currentkey = 0
        for attrib in resultLine:
            user[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return user
    
    def get_user_stats(self):
        cursor = self.getcursor(dictionary=True)

        sql = """
        SELECT 
            COUNT(*) AS total_users,
            ROUND(AVG(age)) AS avg_age
        FROM users
        """
        cursor.execute(sql)
        summary = cursor.fetchone()

        # Inside get_user_stats()
        sql_weight = """
        SELECT 
            COUNT(*) AS total_users,
            ROUND(AVG(age)) AS avg_age,
            (
                SELECT ROUND(AVG(currentBodyWeight - startingBodyWeight), 1)
                FROM users
                WHERE LOWER(goal) = 'Lose Weight'
            ) AS avg_weight_change_loss
        FROM users
        """
        cursor.execute(sql_weight)
        summary = cursor.fetchone()

        sql_top_goals = """
        SELECT goal
        FROM users
        GROUP BY goal
        ORDER BY COUNT(*) DESC
        LIMIT 3
        """
        cursor.execute(sql_top_goals)
        top_goals = [row["goal"] for row in cursor.fetchall()]

        self.closeAll()

        return {
            "total_users": summary["total_users"],
            "avg_age": summary["avg_age"],
            "avg_weight_change_loss": summary["avg_weight_change_loss"],
            "top_goals": top_goals
        }

        
usersDAO = UsersDAO()