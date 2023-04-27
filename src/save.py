import os
from user import *

# Checks if there is an existing user in the /StonksSim/src/saves/ folder. It returns a boolean based on the result
def userFileExists(self):
    path = os.path.dirname(__file__) + "/saves/" + self.username        # fetches path to the saves foleder
    return os.path.exists(path)         

# Creates a file for the user info to be stored in the /StonksSim/src/saves/ folder. Note: Doesn't add any user data to the file, it merely creates a file
def createUserFile(self):
    file = open(os.path.dirname(__file__) + "/saves/" + self.username, "x")     # creates a file in the saves folder
    file.close()
    
# This function writes user data to a file in the /StonksSim/src/saves/ folder named after the user's username
def writeUserData(self):
    file = open(os.path.dirname(__file__) + "/saves/" + self.username, "w")     # opens the save file in the saves folder in write mode
    balance = self.balance
    
    stocks, sell_orders, buy_orders = formatOrders(self)        # formats stock, sell orders and buy orders in an easier format to read

    file.write(str(balance) + "\n" + str(stocks) + "\n" + str(sell_orders) + "\n" + str(buy_orders) + "\n")     # writes all of the data to the file
    file.close()

# This funtion loads all of the user data to a pre-existing user when the program is started. Fields such as balance, stocks, sell orders etc are loaded here.
def loadUserData(self):
    file = open(os.path.dirname(__file__) + "/saves/" + self.username, "r")
    
    data = file.read().split("\n")

    balance = data[0]           # balance data
    stockString = data[1]       # all stocks and their quantity stored in a string in the format: {Stock_symbol_1} {Stock amount_1},{Stock_symbol_2} {Stock amount_2},...,{Stock_symbol_n} {Stock amount_n}
    sellOrderString = data[2]   # all sell orders stored in a string in the format: {Stock_symbol_1} {Stock amount_1} {stock price_1},{Stock_symbol_2} {Stock amount_2} {stock price_2},...,{Stock_symbol_n} {Stock amount_n} {stock price_n}
    buyOrderString = data[3]    # all buy orders stored in a string in the same format as for sell orders

    self.balance = float(balance)           # user balance being set

    allStockInfo = stockString.split(",")
    for i in range(len(allStockInfo) - 1):          # for every unique stock in the array allStockInfo
        stockInfo = allStockInfo[i]
        stockInfoArr = stockInfo.split()
        self.stocks[stockInfoArr[0]] = int(stockInfoArr[1])     # [0]: name of stock/stock_symbol; [1]: amount of a specific stock

    allSellOrderInfo = sellOrderString.split(",")       
    for i in range(len(allSellOrderInfo) - 1):          # for every sell order in the array allSellOrderInfo
        sellOrderInfo = allSellOrderInfo[i]
        sellOrderInfoArr = sellOrderInfo.split()
        self.sell_orders.append(user.order(int(sellOrderInfoArr[1]), float(sellOrderInfoArr[2]), sellOrderInfoArr[0]))      # [1]: amount of stocks to sell; [2]: price per stock in float, [0]: name of stock/stock_symbol

    allBuyOrderInfo = buyOrderString.split(",")     
    for i in range(len(allBuyOrderInfo) - 1):           # for every sell order in the array allBuyOrderInfo
        buyOrderInfo = allBuyOrderInfo[i]
        buyOrderInfoArr = buyOrderInfo.split()
        self.buy_orders.append(user.order(int(buyOrderInfoArr[1]), float(buyOrderInfoArr[2]), buyOrderInfoArr[0]))      # [1]: amount of stocks to sell; [2]: price per stock in float, [0]: name of stock/stock_symbol

    file.close()

# Function for formatting the info from the stocks dicitionary and sell/buy order arrays in order to be more easily readable by the script. Note: this function is meant for private use primarily 
def formatOrders(self):
    stocksString = ""
    for key, value in self.stocks.items():
        stocksString += str(key) + " " + str(value) + ","

    buyOrderString = ""
    for i in range(len(self.buy_orders)):
        order = self.buy_orders[i]
        buyOrderString += order.stock_symbol + " " + str(order.amount) + " " + str(order.price) + ","

    sellOrderString = ""
    for i in range(len(self.sell_orders)):
        order = self.sell_orders[i]
        sellOrderString += order.stock_symbol + " " + str(order.amount) + " " + str(order.price) + ","

    return stocksString, sellOrderString, buyOrderString