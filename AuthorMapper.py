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

    def SearchOperation(self, Choice):
        if Choice=="2":
            squery = 'SELECT Authors.Author_name, Sources.Source_name FROM Authors INNER JOIN Sources ON Authors.Source_id = Sources.Source_id;'
        elif Choice=="3":
            Sname = input("Enter Source name for which you want to see authors : ")
            squery = 'SELECT Authors.Author_name, Sources.Source_name FROM Authors INNER JOIN Sources ON Authors.Source_id = Sources.Source_id WHERE Sources.Source_name = "' + Sname+';'
        else:
            print("Wrong Choice entered")
        self._sqlConnection.executeQuery(squery)

    def UpdateOperation(self, Choice):
        if Choice=="1":
            Aname = input("Enter name of author for who you want to change email : ")
            email = input("Enter new email for ", Aname, " : ")
            squery = 'UPDATE Authors SET email = "' +email+'" WHERE Author_name = "' + Aname+';'
        elif Choice=="2":
            Aname = input("Enter name of author for who you want to change source : ")
            Sname = input("Enter new source name for ", Aname, " : ")
            squery = 'UPDATE Authors SET Source_id = "' +Sname+'" WHERE Author_name = "' + Aname+';'
        else:
            print("Wrong Choice entered")        
        self._sqlConnection.executeQuery(squery)