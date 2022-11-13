class SourceModel:
    def __init__(self):
        self.source_id = None
        self.source_name = None

    def set_source_id(self, sourceid):
        self.source_id = sourceid

    def get_source_id(self):
        return self.source_id


    def set_source_name(self, sourcename):
        self.source_name = sourcename

    def get_source_name(self):
        return self.source_name