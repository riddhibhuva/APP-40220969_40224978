class ReporterModel:
    def __init__(self,data):
        self.reporter_id = data['Reporter_id']
        self.reporter_name = data['Reporter_name']
        self.Email = data['email']
        self.channel_id = data['Channel_id']

    def set_reporter_id(self, repoid):
        self.reporter_id = repoid

    def get_reporter_id(self):
        return self.reporter_id

    def set_reporter_name(self, reponame):
        self.reporter_name = reponame

    def get_reporter_name(self):
        return self.reporter_name

    def set_Email(self, Email):
        self.Email = Email

    def get_Email(self):
        return self.Email

    def set_channel_id(self, channelid):
        self.channel_id = channelid

    def get_channel_id(self):
        return self.channel_id