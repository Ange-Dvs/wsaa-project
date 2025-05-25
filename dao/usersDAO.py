#

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
         
    def getAllUsers(self):
        # Getting all users and converting to a list of dictionaries
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
        # Fetching a user by the ID entered
        cursor = self.getcursor()
        sql="select * from users where userID = %s"
        values = (userID,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def createUser(self, user):
        # Inserting a new user
        cursor = self.getcursor()
        sql="insert into users (firstName, lastName, age, goal) values (%s,%s,%s,%s)"
        values = (
            user.get("firstName"), 
            user.get("lastName"), 
            user.get("age"), 
            user.get("goal"), 
        )
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        user["userID"] = newid
        self.closeAll()
        return user

    def update(self, userID, user):
        # Updating the information for a user
        cursor = self.getcursor()
        sql="""
            update users 
            set firstName= %s,lastName=%s, age=%s, goal=%s 
            where userID = %s
        """
        print(f"update users {user}")
        values = (
            user.get("firstName"), 
            user.get("lastName"), 
            user.get("age"), 
            user.get("goal"), 
            userID
        )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, userID):
        # Deleting a user by user ID
        cursor = self.getcursor()
        sql="delete from users where userID = %s"
        values = (userID,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()     
        print("delete done")

    def convertToDictionary(self, resultLine):
        # Converting results to dictionary
        attkeys=['userID','firstName','lastName', 'age', 'goal']
        user = {}
        currentkey = 0
        for attrib in resultLine:
            user[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return user
    
    def get_user_stats(self):
        # Returning summary statistics for users table and top 3 goals
        cursor = self.getcursor(dictionary=True)

        sql = """
            SELECT 
                COUNT(*) AS total_users,
                ROUND(AVG(age)) AS avg_age
            FROM users
        """
        cursor.execute(sql)
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
            "top_goals": top_goals
        }

usersDAO = UsersDAO()