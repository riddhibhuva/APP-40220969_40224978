from Connect import Database 


class ChannelMapper :
    def __init__(self) :
        self._sqlConnection = Database.getClassObject()
        self._sqlConnection.connect()
    
    def createTable(self):
        squery="CREATE TABLE IF NOT EXISTS Channel(Channel_id INTEGER PRIMARY KEY UNIQUE NOT NULL, Channel_name VARCHAR NOT NULL) "
        self._sqlConnection.executeQuery(squery)

    def insertRow(self, dataObj):
        squery = 'INSERT or IGNORE INTO Channel(Channel_id, Channel_name) VALUES(' + str(dataObj.get_channel_id()) + ',"' + dataObj.get_channel_name() + '"); '
        self._sqlConnection.executeQuery(squery)