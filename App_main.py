from SourceMapper import SourceMapper
from ArticleMapper import ArticleMapper
from AuthorMapper import AuthorMapper
from fastapi import FastAPI
from Connect import Database
from SourceModel import SourceModel
from ArticleModel import ArticleModel
from AuthorModel import AuthorModel

app = FastAPI()

SourceMapper = SourceMapper()
ArticleMapper = ArticleMapper()
AuthorMapper = AuthorMapper()


# @app.post("/")
# async def api_request(json_data:dict):
#     ArticleModel = ArticleMapper(json_data)
#     AuthorModel = AuthorModel(json_data)
#     SourceModel = SourceModel(json_data)
#     SourceMapper.insertRow(dataObj=json_data)
db = Database.getClassObject()
db. connect()

@app.get("/DisplayAllSource")
async def _display_all_sources():
    result_source = SourceMapper.SearchOperation()
    return result_source

@app.get("/Display All Author")
async def _display_all_authors():
    result_author = AuthorMapper.SearchAllOperation()
    return result_author

@app.get("/Display all articles")
async def _display_all_articles():
    result_article = ArticleMapper.SearchAllOperation()
    return result_article

@app.post("/Display All Author for a specific Source")
async def _display_all_author_for_source(data:dict):
    result = AuthorMapper.SearchAuthorOperation(data)
    return {"Author Details": result}

@app.post("/Display Articles of Specific Author")
async def _display_all_articles_for_author(data:dict):
    result = ArticleMapper.SearchAuthorArticlesOperation(data)
    return {"Article Details": result}

@app.post("/Display Articles of Specific Source")
async def _display_all_articles_for_source(data:dict):
    result = ArticleMapper.SearchSourceArticlesOperation(data)
    return {"Article Details": result}



