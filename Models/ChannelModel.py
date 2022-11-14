class ChannelModel:
    def __init__(self,data):
        self.channel_id = data['Channel_id']
        self.channel_name = data['Channel_name']

    def set_channel_id(self, channelid):
        self.channel_id = channelid

    def get_channel_id(self):
        return self.channel_id


    def set_channel_name(self, channelname):
        self.channel_name = channelname

    def get_channel_name(self):
        return self.channel_name