# This is a transactions functions file which will be used in main file

# budget_data = {
#  "balance": 500,
#  "transactions": [
#  {"type": "income", "amount": 1000, "description": "Salary"},
#  {"type": "expense", "amount": 500, "description": "Groceries"}
#  ]
# }

budget_data = {}    # Creating new empty dictionary for all transactions

import random
def user_balance():
    generated_balance = random.randint(100,1000)
    return(generated_balance)


def menu_handler(): # Main Menu Handler
    print("\n" + "*" * 25)
    print("Welcome to Budget Manager")
    print("*" * 25 + "\n")

    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Show Transaction History")
    print("5. Exit")

def add_income():   # Add Income Menu Option
    print("Add Income option has been choosen.")    # For test purposes
    pass    # For test purposes

def add_expense():  # Add Expense Menu Option
    print("Add Expense option has been choosen.")    # For test purposes
    pass    # For test purposes

def show_balance(): # Show Balance Menu Option
    print("Show Balance option has been choosen.")    # For test purposes
    pass    # For test purposes

def show_transaction_history(): # Show Transaction History Menu Option
    print("Show Transaction History option has been choosen.")    # For test purposes
    pass    # For test purposes