import yfinance as yf

def pull_data_realtime(stock_symbol):
    ticker = yf.Ticker(stock_symbol)
    
    # Get historical data
    data = ticker.history(period="1d", interval="1m")
    
    # Alternatively, you can access various stock information
    info = ticker.info
    
    return data, info

print(pull_data_realtime("AAPL"))
23