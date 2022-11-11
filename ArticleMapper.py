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


    def deleteRow(self, choice):
        #print(choice)

        if choice == "1":
            print()
            # Remaining

        elif choice == "2":

            article_id_del=input("Enter the ID of Article you want to delete")
            delquery = 'DELETE From Articles where Article_id = "' + article_id_del + '" ;'
            self._sqlConnection.executeQuery(delquery)

        else:
            print("Wrong Choice enetered")

    def DisplayOperation(self):
        squery = 'SELECT Articles.Title, Articles.Content, Articles.Url, Articles.Published_at, Articles.Country, Authors.Author_name FROM Articles INNER JOIN Authors ON Articles.Author_id = Authors.Author_id;'
        self._sqlConnection.executeQuery(squery)

    def SearchAuthorArticles(self, Aid):
        squery = 'SELECT Articles.Title, Articles.Content, Articles.Url, Articles.Published_at, Articles.Country, Authors.Author_name FROM Articles INNER JOIN Authors ON Articles.Author_id = Authors.Author_id WHERE Authors.Author_id = "' + Aid +'";'
        self._sqlConnection.executeQuery(squery)