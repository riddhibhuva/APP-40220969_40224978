from Connect import Database 

class SourceMappper:
    def __init__(self) :
        self._sqlConnection = Database.getClassObject()
    
    def createTable(self):
        squery="CREATE TABLE Sources(Source_id    INTEGER PRIMARY KEY UNIQUE NOT NULL, Source_name   VARCHAR NOT NULL)"
        self._sqlConnection.execute(squery)
    
    def insertRow(self, dataObj):
        squery = 'INSERT INTO Sources(Source_id, Source_name) VALUES("' + \ dataObj['Source_id']+'","' + dataObj['Source_name']+'");'
        self._sqlConnection.execute(squery)