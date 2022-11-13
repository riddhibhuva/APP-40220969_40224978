class AuthorModel:
    def __init__(self):
        self.author_id = None
        self.author_name = None
        self.Email = None
        self.source_id = None

    def set_author_id(self, authid):
        self.author_id = authid

    def get_author_id(self):
        return self.author_id

    def set_author_name(self, authname):
        self.author_name = authname

    def get_author_name(self):
        return self.author_name

    def set_Email(self, Email):
        self.Email = Email

    def get_Email(self):
        return self.Email

    def set_source_id(self, sourceid):
        self.source_id = sourceid

    def get_source_id(self):
        return self.source_id