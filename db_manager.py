import mysql.connector

class dbmanager():
    def __init__(self):
        self.db_connect()
        self.mycursor = self.mydb.cursor()
        
    def db_connect(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="user1",
            password="user1",
            autocommit = True,
            database = "project"
        )
        
    def execute(self, str):
        self.mycursor.execute(str)
        
    def fetchData(self, str):
        self.mycursor.execute(str)
        data = self.mycursor.fetchall()
        return data