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

    def buy_stocks(self, amount, price, stock_symbol):
        _, _, stock_price = getdata.get_this_week_data(stock_symbol)
        full_price_of_buy = stock_price * amount

        if price != 0:
            if price >= stock_price:
                if self.balance >= full_price_of_buy:
                    self.balance -= full_price_of_buy
                    self.stocks[stock_symbol] = self.stocks.get(stock_symbol, 0) + amount
                    print(f"{self.username} bought {amount} shares of {stock_symbol} at ${stock_price:.2f} each, for a total of ${full_price_of_buy:.2f}.")
                else:
                    print("Insufficient funds")
            else:
                new_order = self.order(amount, price, stock_symbol)
                self.buy_orders.append(new_order)
                print(f"{self.username} placed a buy order for {amount} shares of {stock_symbol} at ${price:.2f} each.")
        else:
            if self.balance >= full_price_of_buy:
                self.balance -= full_price_of_buy
                self.stocks[stock_symbol] = self.stocks.get(stock_symbol, 0) + amount
                print(f"{self.username} bought {amount} shares of {stock_symbol} at ${stock_price:.2f} each, for a total of ${full_price_of_buy:.2f}.")
            else:
                print("Insufficient funds")

    def sell_stocks(self, amount, price, stock_symbol):
        _, _, stock_price = getdata.get_this_week_data(stock_symbol)
        full_price_of_sell = stock_price * amount

        if stock_symbol in self.stocks and self.stocks[stock_symbol] >= amount:
            if price == 0 or price <= stock_price:
                self.balance += full_price_of_sell
                self.stocks[stock_symbol] -= amount
                print(f"{self.username} sold {amount} shares of {stock_symbol} at ${stock_price:.2f} each, for a total of ${full_price_of_sell:.2f}.")

                if self.stocks[stock_symbol] == 0:
                    del self.stocks[stock_symbol]
            else:
                new_order = self.order(amount, price, stock_symbol)
                self.sell_orders.append(new_order)
                print(f"{self.username} placed a sell order for {amount} shares of {stock_symbol} at ${price:.2f} each.")
        else:
            print("Insufficient stocks to sell")


    def gather_stock_symbols_to_check(self):
        stock_symbols = set()
        for order in self.buy_orders + self.sell_orders:
            stock_symbols.add(order.stock_symbol)
        return stock_symbols

    def execute_buy_orders(self, stock_symbol, stock_price):
        buy_orders_to_remove = []
        for buy_order in self.buy_orders:
            if buy_order.stock_symbol == stock_symbol and buy_order.price >= stock_price:
                buy_stocks(self, buy_order.amount, buy_order.price, buy_order.stock_symbol)
                buy_orders_to_remove.append(buy_order)
        return buy_orders_to_remove

    def execute_sell_orders(self, stock_symbol, stock_price):
        sell_orders_to_remove = []
        for sell_order in self.sell_orders:
            if sell_order.stock_symbol == stock_symbol and sell_order.price <= stock_price:
                sell_stocks(self, sell_order.amount, sell_order.price, sell_order.stock_symbol)
                sell_orders_to_remove.append(sell_order)
        return sell_orders_to_remove

    def remove_executed_orders(self, orders_to_remove, order_type):
        for order in orders_to_remove:
            if order_type == 'buy':
                self.buy_orders.remove(order)
            elif order_type == 'sell':
                self.sell_orders.remove(order)

    def check_orders(self):
        stock_symbols_to_check = gather_stock_symbols_to_check(self)

        for stock_symbol in stock_symbols_to_check:
            _, _, stock_price = getdata.get_this_week_data(stock_symbol)

            buy_orders_to_remove = execute_buy_orders(self, stock_symbol, stock_price)
            remove_executed_orders(self, buy_orders_to_remove, 'buy')

            sell_orders_to_remove = execute_sell_orders(self, stock_symbol, stock_price)
            remove_executed_orders(self, sell_orders_to_remove, 'sell')

    def get_orders(self):
        return {
            'buy_orders': self.buy_orders,
            'sell_orders': self.sell_orders
        }

    def remove_order(self, order_type, stock_symbol, price, amount):
        order_list = None

        if order_type.lower() == 'buy':
            order_list = self.buy_orders
        elif order_type.lower() == 'sell':
            order_list = self.sell_orders
        else:
            print("Invalid order type. Please enter 'buy' or 'sell'.")
            return

        for order_item in order_list:
            if (order_item.stock_symbol == stock_symbol and
                    order_item.price == price and
                    order_item.amount == amount):
                order_list.remove(order_item)
                print(f"Removed {order_type} order for {amount} shares of {stock_symbol} at ${price:.2f} each.")
                return

        print(f"No matching {order_type} order found for {amount} shares of {stock_symbol} at ${price:.2f} each.")
