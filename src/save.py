import os
from user import *

# Checks if there is an existing user in the /StonksSim/src/saves/ folder. It returns a boolean based on the result
def userFileExists(self):
    path = os.path.dirname(__file__) + "/saves/" + self.username
    return os.path.exists(path)

# Creates a file for the user info to be stored in the /StonksSim/src/saves/ folder. Note: Doesn't add any user data to the file, it merely creates a file
def createUserFile(self):
    file = open(os.path.dirname(__file__) + "/saves/" + self.username, "x")
    file.close()
    
# This function writes user data to a file in the /StonksSim/src/saves/ folder named after the user's username
def writeUserData(self):
    file = open(os.path.dirname(__file__) + "/saves/" + self.username, "w")
    balance = self.balance
    
    stocks, sell_orders, buy_orders = formatOrders(self)

    file.write(str(balance) + "\n" + str(stocks) + "\n" + str(sell_orders) + "\n" + str(buy_orders) + "\n")
    file.close()

# This funtion loads all of the user data to a pre-existing user when the program is started. Fields such as balance, stocks, sell orders etc are loaded here.
def loadUserData(self):
    file = open(os.path.dirname(__file__) + "/saves/" + self.username, "r")
    
    data = file.read().split("\n")

    balance = data[0]
    stockString = data[1]
    sellOrderString = data[2]
    buyOrderString = data[3]

    self.balance = balance

    allStockInfo = stockString.split(",")
    for i in range(len(allStockInfo) - 1):
        stockInfo = allStockInfo[i]
        stockInfoArr = stockInfo.split()
        self.stocks[stockInfoArr[0]] = int(stockInfoArr[1])

    allSellOrderInfo = sellOrderString.split(",")
    for i in range(len(allSellOrderInfo) - 1):
        sellOrderInfo = allSellOrderInfo[i]
        sellOrderInfoArr = sellOrderInfo.split()
        self.sell_orders.append(user.order(int(sellOrderInfoArr[1]), int(sellOrderInfoArr[2]), sellOrderInfoArr[0]))

    allBuyOrderInfo = buyOrderString.split(",")
    for i in range(len(allBuyOrderInfo) - 1):
        buyOrderInfo = allBuyOrderInfo[i]
        buyOrderInfoArr = buyOrderInfo.split()
        self.buy_orders.append(user.order(int(buyOrderInfoArr[1]), int(buyOrderInfoArr[2]), buyOrderInfoArr[0]))

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