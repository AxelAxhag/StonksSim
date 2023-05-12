
# The python file where the program runs
from interpreter import *
from user import *
from save import *
import threading
import time
import traceback
import datetime


nameInput = input("What is your username?: ").strip()
activeUser = user(nameInput, 0)

def try_catch_create_user(activeUser):
    try:
        balanceInput = input("You're a new user!\nInput a balance to start with: ")
        activeUser.balance = float(balanceInput)
        writeUserData(activeUser)
    except Exception as e:
        print("🚨 Error! Balance must be numbers!")
        file = open(os.path.dirname(__file__) + "/errorlog/" + activeUser.username, "a")
        file.write("Error occured at: " + str(datetime.datetime.now())+ "\n" + traceback.format_exc()+"\n")
        file.close()
        try_catch_create_user(activeUser)

if (userFileExists(activeUser)):
    loadUserData(activeUser)
    print(f"Welcome back, {activeUser.username}!")
    print(f"Your balance is ${activeUser.balance:.2f}.\n")
    activeUser.check_orders_retroactive()
    
else:
    createUserFile(activeUser)
    try_catch_create_user(activeUser)

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
            try:
                commandRead(command, user)
            except Exception as e:
                print("🚨 Command input was invalid or an error occurd, use the 'help' command or check the error logs!")
                file = open(os.path.dirname(__file__) + "/errorlog/" + activeUser.username, "a")
                file.write("Error occured at: " + str(datetime.datetime.now())+ "\n" + traceback.format_exc()+"\n")
                file.close()
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

#Restart thread if crash occurs
while True:
    time.sleep(2)
    if commands_thread.is_alive() == False:
        print("🚨 Restart because of crash")
        commands_thread = threading.Thread(target=process_commands, args=(activeUser, user_lock))
        commands_thread.start()

# Wait for the orders_thread to finish
orders_thread.join()
# Wait for the commands_thread to finish
commands_thread.join()