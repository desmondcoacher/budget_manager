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

def add_income(transactions_database: dict) -> dict: # Add Income Menu Option
    try:
        amount = int(input("Enter income amount: "))
        description = input("Enter income description: ")

        # Update balance
        transactions_database["balance"] += amount

        # Add transaction
        transactions_database["transactions"].append({
            "type": "income",
            "amount": amount,
            "description": description
        })

        print(f"✅ Success: {amount} ₪ for {description} in income transaction type added successfully!\n")

    except ValueError:  # Print error message to the user in case of incorrect value has been choosen
        print("❌ Error: Invalid value. Please enter a number.\n")

    return transactions_database

def add_expense(transactions_database):  # Add Expense Menu Option
    try:
        amount = int(input("Enter income amount: "))
        description = input("Enter income description: ")

        if amount > transactions_database["balance"]:
            print("❌ Error: Insufficient balance.\n")
            return

        # Update balance
        transactions_database["balance"] -= amount

        # Add transaction
        transactions_database["transactions"].append({
            "type": "expense",
            "amount": amount,
            "description": description
        })

        print(f"✅ Success: {amount} ₪ for {description} in expense transaction type added successfully!\n")

    except ValueError:  # Print error message to the user in case of incorrect value has been choosen
        print("❌ Error: Invalid value. Please enter a number.\n")

    return transactions_database

def show_balance(transactions_database): # Show Balance Menu Option
    print(f"ℹ️  Info: Your current balance - {transactions_database["balance"]} ₪.\n")    # Printing message to user with the current balance
    pass    # For test purposes

def show_transaction_history(transactions_database: list): # Show Transaction History Menu Option
    counter: int = 1    # Adding counter for the transactions history displaying sequence
    if not transactions_database["transactions"]:   # In case there are no transactions history
        print("\nℹ️  Info: There are no transactions exists in the database.\n") # Print info message to the user
    else:
        print("\nTransaction List:\n")
        for transaction in transactions_database["transactions"]:
            if transaction["type"] == "income":
                print(f"#{counter} | ⬆️  Type: {transaction["type"].capitalize()} | Amount: {transaction["amount"]} ₪ | Desctiption: {transaction["description"]}")
            else:
                print(f"#{counter} | ⬇️  Type: {transaction["type"].capitalize()} | Amount: {transaction["amount"]} ₪ | Desctiption: {transaction["description"]}")
            counter += 1
        print("")
    
    return transactions_database
    