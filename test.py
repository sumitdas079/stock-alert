from alpha_vantage.timeseries import TimeSeries
def get_stock_data(symbol, api_key):
    """
    Fetch stock data for a given symbol using Alpha Vantage.
    
    Args:
        symbol (str): The stock symbol to fetch data for.
        api_key (str): Your Alpha Vantage API key.
        
    Returns:
        dict: Stock data for the given symbol.
    """
    ts = TimeSeries(key=api_key, output_format='json')
    data, meta_data = ts.get_intraday(symbol=symbol, interval='1min', outputsize='compact')
    return data

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()

    # Get the API key from environment variables
    API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
    
    if not API_KEY:
        raise ValueError("ALPHA_VANTAGE_API_KEY environment variable not set.")
    
    # Example usage
    symbol = "AAPL"  # Example stock symbol
    stock_data = get_stock_data(symbol, API_KEY)
    print(stock_data) 