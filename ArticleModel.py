class ArticleModel:
    def __init__(self):
        self.article_id = None
        self.title = None
        self.content = None
        self.url = None
        self.published_at = None
        self.country = None
        self.author_id = None

    def set_article_id(self, artid):
        self.article_id = artid

    def get_article_id(self):
        return self.article_id

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def set_published_at(self, publishedat):
        self.published_at = publishedat

    def get_published_at(self):
        return self.published_at

    def set_country(self, country):
        self.country = country

    def get_country(self):
        return self.country

    def set_author_id(self, authid):
        self.author_id = authid
        print(authid)
        print(self.author_id)

    def get_author_id(self):
        return self.author_id