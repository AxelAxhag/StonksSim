# Interpreter for interpreting commands through the command line console 
# buy AAPL 10(amount) 200(price per stock)
from user import *
import os
# Switch case for deciding which commands to execute
def commandRead(command, self):
    words = command.split()
    if (len(words) == 3):
        words.append(0)                    # Sets the amount to 0 which says that the stock is listed for the current selling price 
    if(len(words) >=3 ):
        if (int(words[2]) < 1):                      
            print("Cannot buy/sell < 1 stocks!")     # if you set a negative or 0 amount of stocks then give an error
            return
        if (float(words[3]) < 0): 
            print("Cannot sell stocks for < 0!")     # You can't buy stocks for negative money
            return
    match words[0]:
        case "price":
            if(len(words) != 2):
                print("Missing stock symbol")
                return
            _,_,currentPrice = getdata.get_this_week_data(str(words[1]).upper())
            print(f"Price of {str(words[1]).upper()} is ${currentPrice:.2f}")
        case "buy":
            if float(words[3]) == 0:
                _,_,currentPrice = getdata.get_this_week_data(str(words[1]).upper())
                total = currentPrice * int(words[2])
                if input(f"Total price will be ${total:.2f}, are you sure? (Y/N)\n\n> ").strip().upper() != "Y":
                    print("\nDid not buy")
                    return
            print()
            self.buy_stocks(int(words[2]), float(words[3]), str(words[1]).upper())
        case "sell":
            self.sell_stocks(int(words[2]), float(words[3]), str(words[1]).upper())
        case "portfolio":
            self.listPortfolio()
        case "cash":
            balanceAlreadyUsedForOrders = 0
            for buy_order in self.buy_orders:
                balanceAlreadyUsedForOrders += float(buy_order.price) * buy_order.amount
            print(f"💵 BALANCE\n${self.balance:.2f} (🔓 ${self.balance - balanceAlreadyUsedForOrders:.2f})\n")
        case "quit":
            os._exit(0)
        case "exit":
            os._exit(0)
        case "help":
            print("[buy] {name of stock(stocksymbol)} {amount of stocks} {price per stock (optional parameter)}\n[sell] {name of stock(stocksymbol)} {amount of stocks} {price per stock (optional parameter)}\n[cancel] {buy/sell} {order number} -- Cancels a sell/buy order. You get the order number by using the 'portfolio' command\n[portfolio] -- Lists all of the user's balance and stocks\n[price] {name of stock(stocksymbol)} -- Prints the current price of a certain stock\n[cash] -- Prints the user's balance\n[help] -- Prints this prompt for extra help\n[quit] -- Quits/exits the program\n[exit] -- Quits/exits the program\n\nTip: The last parameter in the buy/sell command syntax is optional. If it is blank then the buy/sell order will be set at market price for each stock!")
        case "cancel":
            self.remove_order(words[1], int(words[2]))
        case defualt:
            print(f"The command '{words[0]}' does not exist!\nIf you're struggling with the commands then simply input 'help' into the console!")
