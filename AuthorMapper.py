from Connect import Database 

class AuthorMappper:
    def __init__(self) :
        self._sqlConnection = Database.getClassObject()
    
    def createTable(self):
        squery="CREATE TABLE Authors(Author_id    INTEGER PRIMARY KEY UNIQUE NOT NULL, Author_name   VARCHAR NOT NULL, email   VARCHAR, Source_id   INTEGER NOT NULL, FOREIGN KEY(Source_id) REFERENCES Sources(Source_id))"
        self._sqlConnection.execute(squery)
    
    def insertRow(self, dataObj):
        squery = 'INSERT INTO Authors(Author_id, Author_name, email, Source_id) VALUES("' + \ dataObj['Author_id']+'","' + dataObj['Author_name']+'","' + dataObj['email']+'","' + dataObj['Source_id']+'");'
        self._sqlConnection.execute(squery)