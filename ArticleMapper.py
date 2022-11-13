from Connect import Database 

class ArticleMapper:
    def __init__(self) :
        self._sqlConnection = Database.getClassObject()
    
    def createTable(self):
        squery="CREATE TABLE IF NOT EXISTS Articles(Article_id INTEGER PRIMARY KEY UNIQUE NOT NULL, Title VARCHAR(500) NOT NULL, Content STRING NOT NULL, Url VARCHAR, Published_at VARCHAR, Country VARCHAR, Author_id INTEGER NOT NULL, FOREIGN KEY(Author_id) REFERENCES Author(Author_id))"
        self._sqlConnection.executeQuery(squery)
    
    def insertRow(self, dataObj):
        squery = 'INSERT or IGNORE INTO Articles(Article_id, Title, Content, Url, Published_at, Country, Author_id) VALUES("' + str(dataObj.get_article_id())+'","' + dataObj.get_title()+'","' + dataObj.get_content()+'","' + dataObj.get_url()+'","' + dataObj.get_published_at()+'","' + dataObj.get_country()+'","' + str(dataObj.get_author_id())+'");'
        self._sqlConnection.executeQuery(squery)


    def deleteArticlebydateOperation(self, dataObj):
        squery = 'DELETE From Articles where Published_at = "' + dataObj.get_published_at() + '" ;'
        self._sqlConnection.executeQuery(squery)

    def deleteArticlebyidOperation(self, dataObj):
        squery = 'DELETE From Articles where Article_id = "' + dataObj.get_author_id() + '" ;'
        self._sqlConnection.executeQuery(squery)

    def SearchAllOperation(self):
        squery = 'SELECT Articles.Title, Articles.Content, Articles.Url, Articles.Published_at, Articles.Country, Authors.Author_name FROM Articles INNER JOIN Authors ON Articles.Author_id = Authors.Author_id;'
        result = self._sqlConnection.executeQuery(squery)
        for data in result:
            print(data)

    def SearchAuthorArticlesOperation(self,dataObj):
        squery = 'SELECT Articles.Title, Articles.Content, Articles.Url, Articles.Published_at, Articles.Country, Authors.Author_name FROM Articles INNER JOIN Authors ON Articles.Author_id = Authors.Author_id WHERE Authors.Author_name = "' + dataObj.get_author_name() + '";'
        result = self._sqlConnection.executeQuery(squery)
        for data in result:
            print(data)

    def SearchSourceArticlesOperation(self,dataObj):
        squery = 'SELECT Articles.Title, Articles.Content, Articles.Url, Articles.Published_at, Articles.Country, Authors.Author_name FROM Articles INNER JOIN Authors ON Articles.Author_id = Authors.Author_id WHERE Authors.Source_id = (SELECT Source_id from Sources WHERE Source_name = "' + dataObj.get_source_name() +'");'
        result = self._sqlConnection.executeQuery(squery)
        for data in result:

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

    def insertRowDB(self):
            print(data)
