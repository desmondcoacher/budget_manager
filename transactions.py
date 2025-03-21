# This is a transactions functions file which will be used in main file

def menu_handler(): # Main Menu Handler
    print("\n" + "*" * 25)
    print("Welcome to Budget Manager")
    print("*" * 25 + "\n")

    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Show Transaction History")
    print("5. Exit")

def add_income(amount, description):   # Add Income Menu Option
    print("Add Income option has been choosen.")    # For test purposes
    pass    # For test purposes

def add_expense(amount, description):  # Add Expense Menu Option
    print("Add Expense option has been choosen.")    # For test purposes
    pass    # For test purposes

def show_balance(balance): # Show Balance Menu Option
    print(f"ℹ️  Info: Your current balance - {balance} ₪.\n")    # Printing message to user with the current balance
    pass    # For test purposes

def show_transaction_history(type, amount, description): # Show Transaction History Menu Option
    print("Show Transaction History option has been choosen.")    # For test purposes
    pass    # For test purposes