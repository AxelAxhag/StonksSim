import getdata

class user:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance
        self.stocks = {}
        self.sell_orders = []
        self.buy_orders = []

class order:
    def __init__(self, amount, price, stock_symbol):
        self.amount = amount
        self.price = price
        self.stock_symbol = stock_symbol

def buy_stocks(user, amount, price, stock_symbol):
    _, _, stock_price = getdata.get_this_week_data(stock_symbol)
    full_price_of_buy = stock_price * amount

    if price is not None:
        if price >= stock_price:
            if user.balance >= full_price_of_buy:
                user.balance -= full_price_of_buy
                user.stocks[stock_symbol] = user.stocks.get(stock_symbol, 0) + amount
                print(f"{user.username} bought {amount} shares of {stock_symbol} at ${stock_price:.2f} each, for a total of ${full_price_of_buy:.2f}.")
            else:
                print("Insufficient funds")
        else:
            new_order = order(amount, price, stock_symbol)
            user.buy_orders.append(new_order)
            print(f"{user.username} placed a buy order for {amount} shares of {stock_symbol} at ${price:.2f} each.")
    else:
        if user.balance >= full_price_of_buy:
            user.balance -= full_price_of_buy
            user.stocks[stock_symbol] = user.stocks.get(stock_symbol, 0) + amount
            print(f"{user.username} bought {amount} shares of {stock_symbol} at ${stock_price:.2f} each, for a total of ${full_price_of_buy:.2f}.")
        else:
            print("Insufficient funds")

def sell_stocks(user, amount, price, stock_symbol):
    _, _, stock_price = getdata.get_this_week_data(stock_symbol)
    full_price_of_sell = stock_price * amount

    if stock_symbol in user.stocks and user.stocks[stock_symbol] >= amount:
        if price is None or price <= stock_price:
            user.balance += full_price_of_sell
            user.stocks[stock_symbol] -= amount
            print(f"{user.username} sold {amount} shares of {stock_symbol} at ${stock_price:.2f} each, for a total of ${full_price_of_sell:.2f}.")

            if user.stocks[stock_symbol] == 0:
                del user.stocks[stock_symbol]
        else:
            new_order = order(amount, price, stock_symbol)
            user.sell_orders.append(new_order)
            print(f"{user.username} placed a sell order for {amount} shares of {stock_symbol} at ${price:.2f} each.")
    else:
        print("Insufficient stocks to sell")
