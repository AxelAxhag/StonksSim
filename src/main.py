
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
    balanceInput = input("You're a new user!\nInput a balance to start with: ")
    activeUser.balance = float(balanceInput)
    writeUserData(activeUser)

infoForUser = "📈Welcome to the StonksSimulator📉!\n\nHere you can trade stocks and make yourself a fantasy millionaire if not billionaire.\nThe program is easy to use but in case you need any help then type 'help' in the console!"
print(infoForUser)

# Define the check_orders function that continuously checks for user orders
def check_orders(user, lock):
    while True:
        # Acquire the lock for thread-safe operations
        with lock:
            user.check_orders()
        time.sleep(3)
        

# Define the process_commands function that continuously processes user commands
def process_commands(user, lock):
    while True:
        # Wait for user input as a command
        command = input("\n> ")
        print()
        # Acquire the lock for thread-safe operations
        with lock:
            commandRead(command, user)
            writeUserData(user)

# Create a user_lock object of type threading.Lock for thread-safe operations
user_lock = threading.Lock()

# Initialize the orders_thread with the check_orders function as its target and provide arguments
orders_thread = threading.Thread(target=check_orders, args=(activeUser, user_lock))
# Initialize the commands_thread with the process_commands function as its target and provide arguments
commands_thread = threading.Thread(target=process_commands, args=(activeUser, user_lock))

# Start the orders_thread
orders_thread.start()
# Start the commands_thread
commands_thread.start()

# Wait for the orders_thread to finish
orders_thread.join()
# Wait for the commands_thread to finish
commands_thread.join()