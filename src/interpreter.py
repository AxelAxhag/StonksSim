# Interpreter for interpreting commands through the command line console 
# buy AAPL 10(amount) 200(price per stock)
from user import *

# Switch case for deciding which commands to execute
def commandRead(command, self):
    words = command.split()
    if (len(words) == 3):
        words.append(0)                    # Sets the amount to 0 which says that the stock is listed for the current selling price 
    if(len(words) >=3 ):
        if (int(words[2]) < 1):                      
            print("Cannot buy < 1 stocks!")     # if you set a negative or 0 amount of stocks then give an error
            return
        if (float(words[3]) < 0): 
            print("Cannot sell stocks for < 0!")     # You can't buy stocks for negative money
            return
    match words[0]:
        case "buy":
            self.buy_stocks(int(words[2]), float(words[3]), words[1])
        case "sell":
            self.sell_stocks(int(words[2]), float(words[3]), words[1])
        case "portfolio":
            print(self.stocks)
        case "cash":
            print(self.balance)
        case "logs":
            #TODO add logs to print
            print()
        case defualt:
            print(f"The command '{words[0]}' does not exist")
