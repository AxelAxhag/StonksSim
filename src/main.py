
# The python file where the program runs
from interpreter import *
from user import *
from save import *
import threading
import time


nameInput = input("What is your username?: ").strip()
activeUser = user(nameInput, 0)

if (userFileExists(activeUser)):
    loadUserData(activeUser)
    print(f"Welcome back, {activeUser.username}!")
    print(f"Your balance is ${activeUser.balance:.2f}.\n")
    
else:
    createUserFile(activeUser)
    balanceInput = input("You're a new user! \n Input a balance to start with: ")
    activeUser.balance = balanceInput
    writeUserData(activeUser)

infoForUser = "To buy a stock, the command is 'buy AAPL 10 200' where 'AAPL' is the stock symbol, '10' is the amount of stocks to buy, and '200' is the price per stock.\nTo sell a stock, the command is 'sell AAPL 5 250' where 'AAPL' is the stock symbol, '5' is the amount of stocks to sell, and '250' is the price per stock. \nTo view the user's current portfolio, the command is 'portfolio'."
print(infoForUser)


def check_orders(user, lock):
    while True:
        with lock:
            print("hi")
            user.check_orders()

def process_commands(user, lock):
    while True:
        command = input()
        with lock:
            commandRead(command, user)
            writeUserData(user)

user_lock = threading.Lock()

orders_thread = threading.Thread(target=check_orders, args=(activeUser, user_lock))
commands_thread = threading.Thread(target=process_commands, args=(activeUser, user_lock))

orders_thread.start()
commands_thread.start()

orders_thread.join()
commands_thread.join()