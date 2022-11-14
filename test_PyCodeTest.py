from ChannelMapper import ChannelMapper
from ReporterMapper import ReporterMapper
from ArticleMapper import ArticleMapper
from Connect import Database
from ChannelModel import ChannelModel
from ReporterModel import ReporterModel
from ArticleModel import ArticleModel
import pytest


test_data_json = {"News" :[{"Channel" : [{"Channel_id" : "1","Channel_name" : "BBC-News"}],"Reporters":[{"Reporter_id" : "1","Reporter_name" : "Pranay Parab","email" : "pranay.parab@times.in","Channel_id" : "1"}],"Articles" :[{"Article_id" : "1", "Title" : "Your Mac Has a Hidden White Noise Generator", "Content" : "If you want to drown out environmental noise, or you just like having white noise in the background while you work, you should try your Mac white noise generator. The feature is actually built into every Mac that runs macOS Ventura, you just need to know wh…", "Url" : "https://lifehacker.com/your-mac-has-a-hidden-white-noise-generator-1849760988", "Published_at" : "2022-11-09T16:00:00Z", "Country" : "United States", "Reporter_id" : "1"}]}]}

global __article
global __channel
global __reporter
for item in test_data_json["News"]:
        for data in item["Channel"]:
            __channel = ChannelModel(data)
        for data in item["Reporters"]:
            __reporter = ReporterModel(data)
        for data in item["Articles"]:
            print(data)
            __article = ArticleModel(data)


__ChannelMapper = ChannelMapper()
__ReporterMapper = ReporterMapper()
__ArticleMapper = ArticleMapper()


@pytest.mark.one
def test_data_insert_in_ChannelModel():
    assert __ChannelMapper.insertRow(__channel) is None 

@pytest.mark.one
def test_data_insert_in_ReporterModel():
    assert __ReporterMapper.insertRow(__reporter) is None

@pytest.mark.one
def test_data_insert_in_ArticleModel():
    assert __ArticleMapper.insertRow(__article) is None

@pytest.mark.two
def test_data_display_in_ArticleModel():
    result = __ArticleMapper.SearchAllOperation() 
    assert result is not None

@pytest.mark.three
def test_data_search_in_ReporterModel():
    __channel.set_channel_name("BBC-News") 
    result = __ReporterMapper.SearchReporterOperation(__channel)
    assert result is not None

@pytest.mark.three
def test_data_reporter_in_ArticleModel():
    __reporter.set_reporter_name("Pranay Parab")
    result = __ArticleMapper.SearchReporterArticlesOperation(__reporter) 
    assert result is not None

@pytest.mark.three
def test_data_channel_in_ArticleModel():
    __channel.set_channel_name("BBC-News")
    result = __ArticleMapper.SearchChannelArticlesOperation(__channel) 
    assert result is not None

@pytest.mark.xfail
@pytest.mark.parametrize("Column, Value", [('Name', 'Pranay Parab')])
def test_find_wrong_column(Column, Value):
    assert __reporter[Column] is Value
    print("Test will fail because the column name is wrong")