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


def gather_stock_symbols_to_check(user):
    stock_symbols = set()
    for order in user.buy_orders + user.sell_orders:
        stock_symbols.add(order.stock_symbol)
    return stock_symbols

def execute_buy_orders(user, stock_symbol, stock_price):
    buy_orders_to_remove = []
    for buy_order in user.buy_orders:
        if buy_order.stock_symbol == stock_symbol and buy_order.price >= stock_price:
            buy_stocks(user, buy_order.amount, buy_order.price, buy_order.stock_symbol)
            buy_orders_to_remove.append(buy_order)
    return buy_orders_to_remove

def execute_sell_orders(user, stock_symbol, stock_price):
    sell_orders_to_remove = []
    for sell_order in user.sell_orders:
        if sell_order.stock_symbol == stock_symbol and sell_order.price <= stock_price:
            sell_stocks(user, sell_order.amount, sell_order.price, sell_order.stock_symbol)
            sell_orders_to_remove.append(sell_order)
    return sell_orders_to_remove

def remove_executed_orders(user, orders_to_remove, order_type):
    for order in orders_to_remove:
        if order_type == 'buy':
            user.buy_orders.remove(order)
        elif order_type == 'sell':
            user.sell_orders.remove(order)

def check_orders(user):
    stock_symbols_to_check = gather_stock_symbols_to_check(user)

    for stock_symbol in stock_symbols_to_check:
        _, _, stock_price = getdata.get_this_week_data(stock_symbol)

        buy_orders_to_remove = execute_buy_orders(user, stock_symbol, stock_price)
        remove_executed_orders(user, buy_orders_to_remove, 'buy')

        sell_orders_to_remove = execute_sell_orders(user, stock_symbol, stock_price)
        remove_executed_orders(user, sell_orders_to_remove, 'sell')

