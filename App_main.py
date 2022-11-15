from Mappers.ChannelMapper import ChannelMapper
from Mappers.ArticleMapper import ArticleMapper
from Mappers.ReporterMapper import ReporterMapper
from fastapi import FastAPI
from Connect import Database
from Models.ChannelModel import ChannelModel
from Models.ArticleModel import ArticleModel
from Models.ReporterModel import ReporterModel

app = FastAPI()

ChannelMapper = ChannelMapper()
ArticleMapper = ArticleMapper()
ReporterMapper = ReporterMapper()

db = Database.getClassObject()
db. connect()

@app.get("/Display All Articles")
async def _display_all_articles():
    result_article = ArticleMapper.SearchAllOperation()
    return result_article

@app.post("/Display All Reporters for a specific Channel")
async def _display_all_reporter_for_channel(data:dict):
    result = ReporterMapper.SearchReporterOperation(data)
    return {"Reporter Details": result}

@app.post("/Display Articles of Specific Reporter")
async def _display_all_articles_for_reporter(data:dict):
    result = ArticleMapper.SearchReporterArticlesOperation(data)
    return {"Article Details": result}

@app.post("/Display Articles of Specific Channel")
async def _display_all_articles_for_channel(data:dict):
    result = ArticleMapper.SearchChannelArticlesOperation(data)
    return {"Article Details": result}