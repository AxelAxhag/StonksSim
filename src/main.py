
# The python file where the program runs
from interpreter import *
from user import *
from save import *

nameInput = input("What is your username?: ").strip()
activeUser = user(nameInput, 0)

if (userFileExists(activeUser)):
    loadUserData(activeUser)
    print(f"Welcome back, {activeUser.username}!")
    print(f"Your balance is ${activeUser.balance}.\n")
    
else:
    createUserFile(activeUser)
    balanceInput = input("You're a new user! \n Input a balance to start with: ")
    activeUser.balance = balanceInput


while(True):
    command = input()
    commandRead(command)
    writeUserData(activeUser)

