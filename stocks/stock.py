import requests, os
from icecream import ic
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
# ic(API_KEY)  # Debugging line to print the API key

if not API_KEY:
    raise ValueError("ALPHA_VANTAGE_API_KEY environment variable not set.")

def get_stock_intraday_data(symbol, interval='1min'):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={API_KEY}&outputsize=compact"
    response = requests.get(url)
    # ic(response.json())  # Debugging line to print the response JSON
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}")
    

def get_global_quote(symbol):
    """
    Fetch the global quote for a given stock symbol.
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching global quote: {response.status_code}")
    

def get_daily_data(symbol):
    """
    Fetch daily stock data for a given symbol.
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&outputsize=compact"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching daily data: {response.status_code}")
