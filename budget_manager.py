import transactions  # Importing functions module

# Creating new empty dictionary for all transactions
transactions_database = [
 ()
]
# balance = sum(item[1] if item[0] == "income" else -item[1] for item in transactions)    
balance = 0 # Creating user balance value with starting 0 ₪ on balance

while True: # Loop Menu Start

    transactions.menu_handler() # Calling defined function from transactions imported module (Menu Handler)
    userChoise = input("\nEnter menu option: ") # Asking the user to make a choise

    match userChoise:   # Menu Options Start

        case "1":   # Add Income
            # transactions.add_income(amount, description)   # Calling defined function from transactions imported module
            pass

        case "2":   # Add Expense
            # transactions.add_expense(amount, description)   # Calling defined function from transactions imported module
            pass

        case "3":   # Show Balance
            # transactions.show_balance(balance)   # Calling defined function from transactions imported module
            pass

        case "4":   # Show Transaction History
            # transactions.show_transaction_history(type, amount, description)   # Calling defined function from transactions imported module
            transactions.show_transaction_history(transactions_database)
            
        case "5":   # Exit
            print("Thank you for using our service. See you later!\n")   # Print goodbye message before quit
            break # Breaking the loop (quit)

        case _: # In case that the user's choosen option is not exists
            print("❌ Error: Incorrect menu option has been choosen.\n")   # Print error message in case that incorrect menu option has choosen
    # Menu Options End

    input("Press Enter to return to the Main Menu.")    # Prompt the input message each time into the loop for returning to Main Menu
# Loop Menu End