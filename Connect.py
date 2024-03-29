import sqlite3
from sqlite3 import Error

class Database:
    __classObject = None

    def __init__(self):
        self._DBName = "News.db"
        if Database.__classObject != None:
            raise Exception("Singleton Class error")
        else:
            Database.__classObject = self

    @staticmethod
    def getClassObject():
        if Database.__classObject == None:
            Database()
        return Database.__classObject

    def connect(self):
        sqliteConnection = None
        try:
            sqliteConnection = sqlite3.connect(self._DBName)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if sqliteConnection:
                self.__sqlConnection = sqliteConnection
                print("Database successfully connected")

    def executeQuery(self,query):
        try:
            connection = self.__sqlConnection.execute(query)
            self.__sqlConnection.commit()
            return connection
        except sqlite3.Error as error:
            print("Error:",error)