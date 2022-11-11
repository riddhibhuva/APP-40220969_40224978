from Connect import Database 

class ArticleMapper:
    def __init__(self) :
        self._sqlConnection = Database.getClassObject()
    
    def createTable(self):
        squery="CREATE TABLE IF NOT EXISTS Articles(Article_id INTEGER PRIMARY KEY UNIQUE NOT NULL, Title VARCHAR(500) NOT NULL, Content STRING NOT NULL, Url VARCHAR, Published_at VARCHAR, Country VARCHAR, Author_id INTEGER NOT NULL, FOREIGN KEY(Author_id) REFERENCES Author(Author_id))"
        self._sqlConnection.executeQuery(squery)
    
    def insertRow(self, dataObj):
        for data in dataObj:
            squery = 'INSERT or IGNORE INTO Articles(Article_id, Title, Content, Url, Published_at, Country, Author_id) VALUES("' + data['Article_id']+'","' + data['Title']+'","' + data['Content']+'","' + data['Url']+'","' + data['Published_at']+'","' + data['Country']+'","' + data['Author_id']+'");'
            self._sqlConnection.executeQuery(squery)


    def deleteOperation(self, choice):
        if choice == "1":
            Ddate=input("Enter the date for which you want to delete records : ")
            squery = 'DELETE From Articles where Published_at = "' + Ddate + '" ;'
        elif choice == "2":
            Aid=input("Enter the ID of which you want to delete the article : ")
            squery = 'DELETE From Articles where Article_id = "' + Aid + '" ;'
            self._sqlConnection.executeQuery(squery)
        else:
            print("Wrong Choice enetered")

    def SearchOperation(self,Choice):
        if Choice=="1":
            squery = 'SELECT Articles.Title, Articles.Content, Articles.Url, Articles.Published_at, Articles.Country, Authors.Author_name FROM Articles INNER JOIN Authors ON Articles.Author_id = Authors.Author_id;'
        elif Choice=="2":
            Aname = input("Enter name of author for who you want to search articles : ")
            squery = 'SELECT Articles.Title, Articles.Content, Articles.Url, Articles.Published_at, Articles.Country, Authors.Author_name FROM Articles INNER JOIN Authors ON Articles.Author_id = Authors.Author_id WHERE Authors.Author_name = "' + Aname +'";'
        elif Choice=="2":
            Sname = input("Enter source name for which you want to search articles : ")
            squery = 'SELECT Articles.Title, Articles.Content, Articles.Url, Articles.Published_at, Articles.Country, Authors.Author_name FROM Articles INNER JOIN Authors ON Articles.Author_id = Authors.Author_id WHERE Authors.Source_id = (SELECT Source_id from Sources WHERE Source_name = "' + Sname +'");'
        else:
            print("Wrong Choice enetered")
        self._sqlConnection.executeQuery(squery)