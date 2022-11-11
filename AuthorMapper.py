from Connect import Database 

class AuthorMapper:
    def __init__(self) :
        self._sqlConnection = Database.getClassObject()
    
    def createTable(self):
        squery="CREATE TABLE IF NOT EXISTS Authors(Author_id INTEGER PRIMARY KEY UNIQUE NOT NULL, Author_name VARCHAR NOT NULL, email VARCHAR, Source_id INTEGER NOT NULL, FOREIGN KEY(Source_id) REFERENCES Sources(Source_id))"
        self._sqlConnection.executeQuery(squery)
    
    def insertRow(self, dataObj):
        for data in dataObj:
            squery = 'INSERT or IGNORE INTO Authors(Author_id, Author_name, email, Source_id) VALUES("' + data['Author_id']+'","' + data['Author_name']+'","' + data['email']+'","' + data['Source_id']+'");'
            self._sqlConnection.executeQuery(squery)