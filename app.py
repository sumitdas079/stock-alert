from stocks.stock import get_stock_intraday_data, get_global_quote, get_daily_data
from fastapi import FastAPI

app = FastAPI()

@app.get("/stock/{symbol}")
def read_stock(symbol: str, interval: str = '1min'):
    """
    Fetch intraday stock data for a given symbol and interval.
    """
    try:
        data = get_stock_intraday_data(symbol, interval)
        return data
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/stock/{symbol}/global_quote")
def read_global_quote(symbol: str):
    """
    Fetch the global quote for a given stock symbol.
    """
    try:
        data = get_global_quote(symbol)
        return data
    except Exception as e:
        return {"error": str(e)}

@app.get("/stock/{symbol}/daily_data")
def read_daily_adjusted(symbol: str):
    """
    Fetch daily stock data for a given symbol.
    """
    try:
        data = get_daily_data(symbol)
        return data
    except Exception as e:
        return {"error": str(e)}
    
    
@app.get("/")
def read_root():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "Welcome to the Stock Data API. Use /stock/{symbol} to fetch stock data."}


# read_stock("MSFT", "1min")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0", port=8000)
