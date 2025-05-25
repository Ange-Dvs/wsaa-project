import mysql.connector
import dbconfig as cfg
import datetime

class WeightDAO:
    def __init__(self):
        # Loading database credentials from config file
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    def getcursor(self, dictionary=True):
        # Establishing the connection and returning the cursor
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return self.connection.cursor(dictionary=dictionary)

    def closeAll(self):
        # Closing the database connection
        self.cursor.close()
        self.connection.close()

    def getAllWeights(self):
        # Getting all weight entries in the weight-management table
        self.cursor = self.getcursor()
        self.cursor.execute("SELECT * FROM weight_management ORDER BY currentWeightLogDate DESC")
        results = self.cursor.fetchall()

        # Formatting the date to YYYY-MM-DD
        for row in results:
            if isinstance(row["currentWeightLogDate"], (datetime.date, datetime.datetime)):
                row["currentWeightLogDate"] = row["currentWeightLogDate"].strftime('%Y-%m-%d')

        self.closeAll()
        return results

    def createWeightEntry(self, data):
        # Adding a new weight entry to the table
        self.cursor = self.getcursor()
        sql = """
            INSERT INTO weight_management 
            (userID, currentWeightLogDate, currentBodyWeight, targetBodyWeight, startingBodyWeight)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            data.get("userID"),
            data.get("currentWeightLogDate"),
            data.get("currentBodyWeight"),
            data.get("targetBodyWeight"),
            data.get("startingBodyWeight")
        )
        self.cursor.execute(sql, values)
        self.connection.commit()
        new_id = self.cursor.lastrowid
        self.closeAll()
        return {"id": new_id}

    def updateWeightEntry(self, id, data):
        # Updating an existing weight entry
        self.cursor = self.getcursor()
        sql = """
            UPDATE weight_management
            SET userID=%s, currentWeightLogDate=%s, currentBodyWeight=%s, 
                targetBodyWeight=%s, startingBodyWeight=%s
            WHERE id=%s
        """
        values = (
            data.get("userID"),
            data.get("currentWeightLogDate"),
            data.get("currentBodyWeight"),
            data.get("targetBodyWeight"),
            data.get("startingBodyWeight"),
            id
        )
        self.cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def deleteWeightEntry(self, id):
        # Deleting a weight entry
        self.cursor = self.getcursor()
        sql = "DELETE FROM weight_management WHERE id=%s"
        self.cursor.execute(sql, (id,))
        self.connection.commit()
        self.closeAll()

weightDAO = WeightDAO()