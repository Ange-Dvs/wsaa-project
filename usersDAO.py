# boook dao 
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
         
    def getAll(self):
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

    def create(self, user):
        cursor = self.getcursor()
        sql="insert into users (firstName, lastName, age, goal, startingWeight, currentWeight) values (%s,%s,%s,%s,%s,%s)"
        values = (user.get("firstName"), user.get("lastName"), user.get("age"), user.get("goal"), user.get("startingWeight"), user.get("currentWeight"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        user["userID"] = newid
        self.closeAll()
        return user


    def update(self, userID, user):
        cursor = self.getcursor()
        sql="update users set firstName= %s,lastName=%s, age=%s, goal=%s, startingWeight=%s, currentWeight=%s  where userID = %s"
        print(f"update users {user}")
        values = (user.get("firstName"), user.get("lastName"), user.get("age"), user.get("goal"), user.get("startingWeight"), user.get("currentWeight"), userID)
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
        attkeys=['userID','firstName','lastName', 'age', 'goal', 'startingWeight', 'currentWeight']
        user = {}
        currentkey = 0
        for attrib in resultLine:
            user[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return user

        
usersDAO = UsersDAO()