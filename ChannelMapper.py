from Connect import Database 


class ChannelMapper :
    def __init__(self) :
        self._sqlConnection = Database.getClassObject()
    
    def createTable(self):
        squery="CREATE TABLE IF NOT EXISTS Channels(Channel_id INTEGER PRIMARY KEY UNIQUE NOT NULL, Channel_name VARCHAR NOT NULL) "
        self._sqlConnection.executeQuery(squery)

    def insertRow(self, dataObj):
        squery = 'INSERT or IGNORE INTO Channels(Channel_id, Channel_name) VALUES(' + str(dataObj.get_channel_id()) + ',"' + dataObj.get_channel_name() + '"); '
        self._sqlConnection.executeQuery(squery)

    def SearchOperation(self):
        squery = 'SELECT * FROM Channels;'
        result = self._sqlConnection.executeQuery(squery)
        column_name = ["Channel_id","Channel_name"]
        final = []
        for data in result:
            temp = dict(zip(column_name, data))
            final.append(temp)
        return (final)