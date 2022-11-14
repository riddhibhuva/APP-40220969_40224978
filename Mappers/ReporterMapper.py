from Connect import Database 

class ReporterMapper:
    def __init__(self) :
        self._sqlConnection = Database.getClassObject()
        self._sqlConnection.connect()
    
    def createTable(self):
        squery="CREATE TABLE IF NOT EXISTS Reporters(Reporter_id INTEGER PRIMARY KEY UNIQUE NOT NULL, Reporter_name VARCHAR NOT NULL, email VARCHAR, Channel_id INTEGER NOT NULL, FOREIGN KEY(Channel_id) REFERENCES Channels(Channel_id))"
        self._sqlConnection.executeQuery(squery)
    
    def insertRow(self, dataObj):
        squery = 'INSERT or IGNORE INTO Reporters(Reporter_id, Reporter_name, email, Channel_id) VALUES("' + str(dataObj.get_reporter_id()) +'","' + dataObj.get_reporter_name() +'","' + dataObj.get_Email() +'","' + str(dataObj.get_channel_id()) + '");'
        self._sqlConnection.executeQuery(squery)

    def SearchAllOperation(self):
        squery = 'SELECT Reporters.Reporter_id, Reporters.Reporter_name, Reporters.email, Channels.Channel_name FROM Reporters INNER JOIN Channels ON Reporters.Channel_id = Channels.Channel_id;'
        result = self._sqlConnection.executeQuery(squery)
        column_name = ["Reporter_id", "Reporter_name", "email", "Channel_name"]
        final = []
        for data in result:
            temp = dict(zip(column_name, data))
            final.append(temp)
        return (final)

        # for data in result:
        #     print(data)

    def SearchReporterOperation(self, dataObj):
        squery = 'SELECT Reporters.Reporter_name, Channels.Channel_name FROM Reporters INNER JOIN Channels ON Reporters.Channel_id = Channels.Channel_id WHERE Channels.Channel_name = "' + str(dataObj['Channel_name'])+'";'
        result = self._sqlConnection.executeQuery(squery)
        column_name = ["Reporter_name", "Channel_name"]
        final = []
        for data in result:
            temp = dict(zip(column_name, data))
            final.append(temp)
        return final

        # for data in result:
        #     print(data)

    # def UpdateEmailOperation(self, dataObj):
    #     squery = 'UPDATE Authors SET email = "' +dataObj.get_Email()+'" WHERE Author_name = "' + dataObj.get_author_name()+'";'
    #     self._sqlConnection.executeQuery(squery)
    #
    # def UpdateSourceOperation(self, AdataObj, SdataObj):
    #     squery = 'UPDATE Authors SET Source_id = (SELECT Source_id FROM Sources WHERE Source_name = "' +SdataObj.get_source_name()+'") WHERE Author_name = "' + AdataObj.get_author_name()+'";'
    #     self._sqlConnection.executeQuery(squery)