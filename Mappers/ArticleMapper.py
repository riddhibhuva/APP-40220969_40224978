from Connect import Database 

class ArticleMapper:
    def __init__(self) :
        self._sqlConnection = Database.getClassObject()
        self._sqlConnection.connect()
    
    def createTable(self):
        squery="CREATE TABLE IF NOT EXISTS Articles(Article_id INTEGER PRIMARY KEY UNIQUE NOT NULL, Title VARCHAR(500) NOT NULL, Content STRING NOT NULL, Url VARCHAR, Published_at VARCHAR, Country VARCHAR, Reporter_id INTEGER NOT NULL, FOREIGN KEY(Reporter_id) REFERENCES Author(Reporter_id))"
        self._sqlConnection.executeQuery(squery)
    
    def insertRow(self, dataObj):
        squery = 'INSERT or IGNORE INTO Articles(Article_id, Title, Content, Url, Published_at, Country, Reporter_id) VALUES("' + str(dataObj.get_article_id())+'","' + dataObj.get_title()+'","' + dataObj.get_content()+'","' + dataObj.get_url()+'","' + dataObj.get_published_at()+'","' + dataObj.get_country()+'","' + str(dataObj.get_reporter_id())+'");'
        self._sqlConnection.executeQuery(squery)


    # def deleteArticlebydateOperation(self, dataObj):
    #     squery = 'DELETE From Articles where Published_at = "' + dataObj.get_published_at() + '" ;'
    #     self._sqlConnection.executeQuery(squery)
    #
    # def deleteArticlebyidOperation(self, dataObj):
    #     squery = 'DELETE From Articles where Article_id = "' + dataObj.get_author_id() + '" ;'
    #     self._sqlConnection.executeQuery(squery)

    def SearchAllOperation(self):
        squery = 'SELECT Articles.Article_id, Articles.Title, Articles.Content, Articles.Url, Articles.Published_at, Articles.Country, Reporters.Reporter_name FROM Articles INNER JOIN Reporters ON Articles.Reporter_id = Reporters.Reporter_id;'
        result = self._sqlConnection.executeQuery(squery)
        column_name = ["Article_id","Title","content","Url","Published_at","Country","Reporter_name"]
        final = []
        for data in result:
            temp = dict(zip(column_name, data))
            final.append(temp)
        return (final)
        # for data in result:
        #     print(data)

    def SearchReporterArticlesOperation(self, dataObj):
        squery = 'SELECT Articles.Title, Articles.Content, Articles.Url, Articles.Published_at, Articles.Country, Reporters.Reporter_name FROM Articles INNER JOIN Reporters ON Articles.Reporter_id = Reporters.Reporter_id WHERE Reporters.Reporter_name = "' + str(dataObj.get_reporter_name) + '";'
        result = self._sqlConnection.executeQuery(squery)
        column_name = ["Title", "Content", "Url","Published_at", "Country", "Reporter_name"]
        final = []
        for data in result:
            temp = dict(zip(column_name, data))
            final.append(temp)
        return final
        # for data in result:
        #     print(data)

    def SearchChannelArticlesOperation(self, dataObj):
        squery = 'SELECT Articles.Title, Articles.Content, Articles.Url, Articles.Published_at, Articles.Country, Reporters.Reporter_name FROM Articles INNER JOIN Reporters ON Articles.Reporter_id = Reporters.Reporter_id ' \
                 'WHERE Reporters.Channel_id = (SELECT Channel_id from Channels WHERE Channel_name = "' + str(dataObj.get_channel_name) +'");'
        result = self._sqlConnection.executeQuery(squery)
        column_name = ["Title", "Content", "Url", "Published_at", "Country", "Reporter_name"]
        final = []
        for data in result:
            temp = dict(zip(column_name, data))
            final.append(temp)
        return final

        # for data in result:
        #     print(data)