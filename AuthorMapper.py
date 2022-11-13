from Connect import Database 

class AuthorMapper:
    def __init__(self) :
        self._sqlConnection = Database.getClassObject()
    
    def createTable(self):
        squery="CREATE TABLE IF NOT EXISTS Authors(Author_id INTEGER PRIMARY KEY UNIQUE NOT NULL, Author_name VARCHAR NOT NULL, email VARCHAR, Source_id INTEGER NOT NULL, FOREIGN KEY(Source_id) REFERENCES Sources(Source_id))"
        self._sqlConnection.executeQuery(squery)
    
    def insertRow(self, dataObj):
        squery = 'INSERT or IGNORE INTO Authors(Author_id, Author_name, email, Source_id) VALUES("' + str(dataObj.get_author_id())+'","' + dataObj.get_author_name()+'","' + dataObj.get_Email()+'","' + str(dataObj.get_source_id())+'");'
        self._sqlConnection.executeQuery(squery)

    def SearchAllOperation(self):
        squery = 'SELECT Authors.Author_name, Authors.email, Sources.Source_name FROM Authors INNER JOIN Sources ON Authors.Source_id = Sources.Source_id;'
        result = self._sqlConnection.executeQuery(squery)
        for data in result:
            print(data)

    def SearchAuthorOperation(self, dataObj):
        squery = 'SELECT Authors.Author_name, Sources.Source_name FROM Authors INNER JOIN Sources ON Authors.Source_id = Sources.Source_id WHERE Sources.Source_name = "' + dataObj.get_source_name()+'";'
        result = self._sqlConnection.executeQuery(squery)

        for data in result:
            print(data)

    def UpdateEmailOperation(self, dataObj):
        squery = 'UPDATE Authors SET email = "' +dataObj.get_Email()+'" WHERE Author_name = "' + dataObj.get_author_name()+'";'
        self._sqlConnection.executeQuery(squery)

    def UpdateSourceOperation(self, AdataObj, SdataObj):
        squery = 'UPDATE Authors SET Source_id = (SELECT Source_id FROM Sources WHERE Source_name = "' +SdataObj.get_source_name()+'") WHERE Author_name = "' + AdataObj.get_author_name()+'";'
        self._sqlConnection.executeQuery(squery)