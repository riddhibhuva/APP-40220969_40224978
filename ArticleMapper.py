from Connect import Database 

class ArticleMappper:
    def __init__(self) :
        self._sqlConnection = Database.getClassObject()
    
    def createTable(self):
        squery="CREATE TABLE Articles(Article_id    INTEGER PRIMARY KEY UNIQUE NOT NULL, Title   VARCHAR(500) NOT NULL, Content   STRING NOT NULL, url   VARCHAR, Published_at   VARCHAR, Country   VARCHAR, Author_id   INTEGER NOT NULL, FOREIGN KEY(Author_id) REFERENCES Author(Author_id))"
        self._sqlConnection.execute(squery)
    
    def insertRow(self, dataObj):
        squery = 'INSERT INTO Authors(Article_id, Title, Content, url, Published_at, Author_id) VALUES("' + dataObj['Article_id']+'","' + dataObj['Title']+'","' + dataObj['Content']+'","' + dataObj['url']+'","' + dataObj['Country']+'","' + dataObj['Author_id']+'");'
        self._sqlConnection.execute(squery)