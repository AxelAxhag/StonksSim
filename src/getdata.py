import yfinance as yf
import datetime

def pull_data_realtime(stock_symbol):
    ticker = yf.Ticker(stock_symbol)
    
    # Get historical data
    data = ticker.history(period="1d", interval="1m")
    
    # Alternatively, you can access various stock information
    info = ticker.info
    
    return data, info

def pull_this_week_data(stock_symbol):
    current_time = datetime.datetime.now()
    oneWeekAgo = current_time - datetime.timedelta(days=7)
    ticker = yf.Ticker(stock_symbol)
    data = ticker.history(interval='5m',start=oneWeekAgo,end=current_time)
    return data.head()

#infoApple = pull_data_realtime("AAPL")
print(pull_this_week_data("AAPL"))

def print_short_info(info):
    info = info[1]  # Access the dictionary from the tuple
    print("Company Name:", info["shortName"])
    print("Industry:", info["industry"])
    print("Market Cap:", info["marketCap"])
    print("52-week High:", info["fiftyTwoWeekHigh"])
    print("52-week Low:", info["fiftyTwoWeekLow"])

#print_short_info(infoApple)

