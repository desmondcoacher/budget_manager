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

def add_income(budget_data: dict) -> dict:
    """
    Adds an income transaction to the budget_data dictionary.
    Updates balance and appends to transactions list.
    """
    try:
        amount = float(input("Enter income amount: "))
        description = input("Enter income description: ")

        # Update balance
        budget_data["balance"] += amount

        # Add transaction
        budget_data["transactions"].append({
            "type": "income",
            "amount": amount,
            "description": description
        })

        print(f"✅ Income of {amount} added successfully!")

    except ValueError:
        print("❌ Invalid amount. Please enter a number.")

    return budget_data

def add_expense(amount, description):  # Add Expense Menu Option
    print("Add Expense option has been choosen.")    # For test purposes
    pass    # For test purposes

def show_balance(balance): # Show Balance Menu Option
    print(f"ℹ️  Info: Your current balance - {balance} ₪.\n")    # Printing message to user with the current balance
    pass    # For test purposes

def show_transaction_history(transactions_database: list): # Show Transaction History Menu Option
    counter: int = 1
    for transaction in transactions_database:
        print(f"{counter} - {transaction}")
    
    return transactions_database
    