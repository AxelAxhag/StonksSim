from user import *
global user

u1 = user("felix", 10000000)
buy_stocks(u1, 10, 170, "AAPL")
sell_stocks(u1, 5, None, "AAPL")
sell_stocks(u1, 7, None, "AAPL")
buy_stocks(u1, 1000, None, "AAPL")
print(u1.stocks)