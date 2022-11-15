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

    def SearchReporterOperation(self, dataObj):
        squery = 'SELECT Reporters.Reporter_name, Channels.Channel_name FROM Reporters INNER JOIN Channels ON Reporters.Channel_id = Channels.Channel_id WHERE Channels.Channel_name = "' + str(dataObj['Channel_name'])+'";'
        result = self._sqlConnection.executeQuery(squery)
        column_name = ["Reporter_name", "Channel_name"]
        final = []
        for data in result:
            temp = dict(zip(column_name, data))
            final.append(temp)
        return final