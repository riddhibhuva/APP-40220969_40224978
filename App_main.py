from ChannelMapper import ChannelMapper
from ArticleMapper import ArticleMapper
from ReporterMapper import ReporterMapper
from fastapi import FastAPI
from Connect import Database
from ChannelModel import ChannelModel
from ArticleModel import ArticleModel
from ReporterModel import ReporterModel

app = FastAPI()

ChannelMapper = ChannelMapper()
ArticleMapper = ArticleMapper()
ReporterMapper = ReporterMapper()


# @app.post("/")
# async def api_request(json_data:dict):
#     ArticleModel = ArticleMapper(json_data)
#     AuthorModel = AuthorModel(json_data)
#     SourceModel = SourceModel(json_data)
#     SourceMapper.insertRow(dataObj=json_data)
db = Database.getClassObject()
db. connect()

# @app.get("/Display All Channels")
# async def _display_all_channel():
#     result_source = ChannelMapper.SearchOperation()
#     return result_source
#
# @app.get("/Display All Reporters")
# async def _display_all_reporter():
#     result_author = ReporterMapper.SearchAllOperation()
#     return result_author

@app.get("/Display All Articles")
async def _display_all_articles():
    result_article = ArticleMapper.SearchAllOperation()
    return result_article

@app.post("/Display All Reporters for a specific Channel")
async def _display_all_reporter_for_channel(data:dict):
    result = ReporterMapper.SearchReporterOperation(data)
    return {"Author Details": result}

@app.post("/Display Articles of Specific Reporter")
async def _display_all_articles_for_reporter(data:dict):
    result = ArticleMapper.SearchReporterArticlesOperation(data)
    return {"Article Details": result}

@app.post("/Display Articles of Specific Channel")
async def _display_all_articles_for_channel(data:dict):
    result = ArticleMapper.SearchChannelArticlesOperation(data)
    return {"Article Details": result}



