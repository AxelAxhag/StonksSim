import yfinance as yf
import datetime
import pandas as pd
import time

data_cache = {} #Store fetched data

# Function to pull real-time data for a stock symbol
def pull_data_realtime(stock_symbol):
    ticker = yf.Ticker(stock_symbol)
    
    # Get historical data
    data = ticker.history(period="1d", interval="1m")
    
    # Alternatively, you can access various stock information
    info = ticker.info
    
    return data, info

# Function to pull the last week's stock data for a stock symbol, and realtime
def pull_this_week_data(stock_symbol):
    current_time = datetime.datetime.now()
    oneWeekAgo = current_time - datetime.timedelta(days=7)
    ticker = yf.Ticker(stock_symbol)
    data = ticker.history(interval='5m',start=oneWeekAgo,end=current_time)

    # Process and reformat the DataFrame
    data.reset_index(inplace=True) # Reset the index of the DataFrame with data.reset_index(inplace=True), so that the DateTime index becomes a regular column.
    data['Date'] = data['Datetime'].dt.date # Create two new columns, 'Date' and 'Time', by extracting the date and time components from the 'Datetime' column using data['Datetime'].dt.date and data['Datetime'].dt.time, respectively.
    data['Time'] = data['Datetime'].dt.time 
    data = data[['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']] # Rearrange the columns to a more readable format, keeping only the necessary columns, using data = data[['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']].
    
    closing_price = data['Close'].iloc[-1]
    maxLastWeek = data['High'].max()
    return data, maxLastWeek, closing_price #Returns a pandas DataFrame, containing columns for date, time, open, high, low, close, and volume for each 5 min last week. And last closing

""" Explanation of a pandas DataFrame:
    Here are some key features and concepts related to pandas DataFrames:

    Index and columns: A DataFrame has an index (row labels) and columns (column labels). By default, the index is a range of integers (0, 1, 2, ...), but you can also set a custom index, such as a date or other unique identifier. Columns represent different variables/features in the data.
    Data types: Each column in a DataFrame can store a different data type, such as integers, floats, strings, or datetime objects. This allows for a mix of data types in a single DataFrame.
    Selection and slicing: You can easily select and slice data in a DataFrame using labels, positions, or conditions. For example, you can select specific columns, rows, or subsets of data that meet certain criteria.
    Manipulation: DataFrames offer a variety of functions for data manipulation, such as merging, joining, concatenating, pivoting, reshaping, and more. You can also apply custom functions or perform arithmetic operations on columns.
    Handling missing data: Pandas provides tools for handling missing data, such as filling missing values with default values, interpolating, or dropping rows/columns with missing data.
    Grouping and aggregation: With pandas, you can easily group data by one or more columns and perform aggregation functions, such as sum, mean, count, etc., on the grouped data.
    Sorting: You can sort a DataFrame by one or multiple columns, in ascending or descending order.
    Importing and exporting data: Pandas supports importing and exporting data from/to various file formats, such as CSV, Excel, JSON, SQL, and more."""

# Function to get the last week's stock data for a stock symbol
# with caching and cache duration (default: 15 minutes)
def get_this_week_data(stock_symbol, cache_duration=900):  # cache_duration is in seconds (default: 15 min)
    current_time = time.time()
    if stock_symbol not in data_cache or current_time - data_cache[stock_symbol]["timestamp"] > cache_duration:
        data, maxLastWeek, closing_price = pull_this_week_data(stock_symbol)
        data_cache[stock_symbol] = {
            "data": (data, closing_price, maxLastWeek),
            "timestamp": current_time
        }
    
    return data_cache[stock_symbol]["data"]

# Function to print short information about a stock
def print_short_info(info):
    info = info[1]  # Access the dictionary from the tuple
    print("Company Name:", info["shortName"])
    print("Industry:", info["industry"])
    print("Market Cap:", info["marketCap"])
    print("52-week High:", info["fiftyTwoWeekHigh"])
    print("52-week Low:", info["fiftyTwoWeekLow"])

# Get max of stock during a specific time interval
def get_max_stock_value(ticker, start_date, end_date):
    stock_data = yf.download(ticker, interval="5m", start=start_date, end=end_date, progress=False, show_errors=False)
    if stock_data.empty:
        _,_,last_closing_price  = get_this_week_data(ticker)
        return last_closing_price
    max_value = stock_data['Adj Close'].max()
    return max_value

# Get min of stock during a specific time interval
def get_min_stock_value(ticker, start_date, end_date):
    stock_data = yf.download(ticker, interval="5m", start=start_date, end=end_date, progress=False, show_errors=False)
    if stock_data.empty:
        _,_, last_closing_price = get_this_week_data(ticker)
        return last_closing_price
    min_value = stock_data['Adj Close'].min()
    return min_value
