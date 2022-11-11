from Connect import Database 


class SourceMapper :
    def __init__(self) :
        self._sqlConnection = Database.getClassObject()
    
    def createTable(self):
        squery="CREATE TABLE IF NOT EXISTS Sources(Source_id INTEGER PRIMARY KEY UNIQUE NOT NULL, Source_name VARCHAR NOT NULL) "
        self._sqlConnection.executeQuery(squery)
    
    def insertRow(self, dataObj):
        #print(dataObj)
        for data in dataObj:
            squery = 'INSERT or IGNORE INTO Sources(Source_id, Source_name) VALUES('+str(data['Source_id'])+',"' + data['Source_name']+'"); '
            self._sqlConnection.executeQuery(squery)