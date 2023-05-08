# StonksSim
## Overview

> **Note**: The stocks available are only stocks that are list by NASDAQ!  

The Stonk Simulator is a Python-based program that allows users to engage in a virtual stock market environment, enabling them to buy and sell fake stocks from real companies. By leveraging the Yahoo Finance API, the simulator provides users with up-to-date and accurate market data, offering an engaging and educational experience for anyone interested in learning about stock trading and investment strategies. 

### How to Run the Simulator

1. Clone this repository to your local machine.
2. Open a terminal/command prompt window and navigate to the directory where you cloned the repository.
3. Install the required dependencies by running the following command: `pip install -r requirements.txt`
4. Start the simulator by running the following command: `python3 src/main.py`


### How to Use the Simulator

Once the simulator is running, you can enter commands into the console to perform various actions. The available commands are:

- `buy {stock symbol} {amount} {price}`: Buy a certain amount of a stock at a specific price.
- `sell {stock symbol} {amount} {price}`: Sell a certain amount of a stock at a specific price.
- `portfolio`: View your current portfolio of stocks.
- `cash`: View your current balance.
- `cancel {'buy'/'sell'} {buy/sell order number}`: Cancels a buy or sell order. In order to get the order number, use the `portfolio` command and check the left handside where the order number is listed after the '#' symbol
- `help`: Display a list of available commands and their syntax.
- `quit` or `exit`: Exit the simulator.

Note that the `buy` and `sell` commands require you to specify the stock symbol (e.g., AAPL for Apple), the amount of stock you want to buy/sell, and the price you want to buy/sell it for. If you don't specify a price, the order will be executed at the current market price.

### How the Simulator Works

The simulator uses a simple object-oriented design to manage user accounts and simulate the buying and selling of stocks. Each user account has a balance and a portfolio of stocks that they own. When a user buys or sells a stock, their balance and portfolio are updated accordingly.

The simulator also includes a command interpreter that reads user input from the console and executes the appropriate command. The command interpreter uses a switch statement to determine which command to execute based on the first word of the user's input.

Overall, the simulator provides a simple way for users to learn about the stock market and practice making trades without risking real money.
