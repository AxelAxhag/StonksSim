
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

user1 = input()
u1 = user(user1, 10000)


while(True):
    command = input()

    commandRead(command)
    writeUserData(activeUser)


