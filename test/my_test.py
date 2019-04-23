from app.source.Alpha import GetStockInfo
from app.source.NYTimes import GetNYTArticles
from app.source.OpenWeatherMap import getWeatherInfo
from app.source.SportRadar import getSportsInfo
from app.spreadsheet import get_products

def test_Get_Stock():
    stock = GetStockInfo("NKE")
    assert stock == ""
    assert stock != "Sorry we can't find any trading data for NKE."
    assert stock != "Something unexpected went wrong while gathering stock information."

def test_Get_News():
    news = GetNYTArticles()
    assert news != ""
    assert news != "Sorry we can't gather news information at this moment"
    assert news != "Something unexpected went wrong while gathering news information."

def test_Get_Weather():
    weather = getWeatherInfo("59718")
    assert weather != ""
    assert weather != "Sorry we can't gather weather information at this moment"
    assert weather != "Something unexpected went wrong while gathering weather information."

def test_Get_Sports():
    sports = getSportsInfo("NFL")
    assert sports != ""
    assert sports != "Sorry we can't gather sports information at this moment"
    assert sports != "Something unexpected went wrong while gathering sports information."

    sports = getSportsInfo("NBA")
    assert sports != ""
    assert sports != "Sorry we can't gather sports information at this moment"
    assert sports != "Something unexpected went wrong while gathering sports information."

    sports = getSportsInfo("NHL")
    assert sports != ""
    assert sports != "Sorry we can't gather sports information at this moment"
    assert sports != "Something unexpected went wrong while gathering sports information."

    sports = getSportsInfo("MLB")
    assert sports != ""
    assert sports != "Sorry we can't gather sports information at this moment"
    assert sports != "Something unexpected went wrong while gathering sports information."

def test_spreadsheet():
    spreadsheet = get_products()
    assert spreadsheet != []



