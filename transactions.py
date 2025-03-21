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

def add_income(transactions_database: dict) -> dict:
    """
    Adds an income transaction to the transactions_database dictionary.
    Updates balance and appends to transactions list.
    """
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

        print(f"✅ Success: {amount} ₪ for {description} in income transaction type added successfully!")

    except ValueError:
        print("❌ Invalid amount. Please enter a number.")

    return transactions_database

# def add_expense(transactions_database):  # Add Expense Menu Option
#     print("Add Expense option has been choosen.")    # For test purposes
#     pass    # For test purposes

def show_balance(transactions_database): # Show Balance Menu Option
    print(f"ℹ️  Info: Your current balance - {transactions_database["balance"]} ₪.\n")    # Printing message to user with the current balance
    pass    # For test purposes

def show_transaction_history(transactions_database: list): # Show Transaction History Menu Option
    counter: int = 1
    if not transactions_database["transactions"]:
        print("\nℹ️  Info: There are no transactions exists in the database.\n")
    else:
        print("\nTransaction List:\n")
        for transaction in transactions_database["transactions"]:
            print(f"#{counter} | Type: {transaction["type"].capitalize()} | Amount: {transaction["amount"]} ₪ | Desctiption: {transaction["description"]}")
            counter += 1
        print("")
    
    return transactions_database
    