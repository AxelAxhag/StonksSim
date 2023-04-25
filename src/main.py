
# The python file where the program runs
from interpreter import *
from user import *


user1 = input()
u1 = user(user1, 10000)


while(True):
    command = input()
    commandRead(command, u1)

