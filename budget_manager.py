# budget_data = {
#  "balance": 500,
#  "transactions": [
#  {"type": "income", "amount": 1000, "description": "Salary"},
#  {"type": "expense", "amount": 500, "description": "Groceries"}
#  ]
# }

import transactions  # Importing functions module

budget_data = {}    # Creating new empty dictionary for all transactions

while True: # Loop Menu Start

    transactions.menu_handler() # Calling defined function from transactions imported module (Menu Handler)
    
    userChoise = input("\nEnter menu option: ") # # Asking the user to make a choise

    match userChoise:   # Menu Options Start

        case "1":   # Add Income
            print("Menu option 1 has been choosen.")
            # pass
            transactions.add_income()   # Calling defined function from transactions imported module

        case "2":   # Add Expense
            print("Menu option 2 has been choosen.")
            # pass
            transactions.add_expense()   # Calling defined function from transactions imported module

        case "3":   # Show Balance
            print("Menu option 3 has been choosen.")
            # pass
            transactions.show_balance()   # Calling defined function from transactions imported module

        case "4":   # Show Transaction History
            print("Menu option 4 has been choosen.")
            # pass
            transactions.show_transaction_history()   # Calling defined function from transactions imported module

        case "5":   # Exit
            print("Thank you for using our service. See you later!\n")   # Print goodbye message before quit
            break # Breaking the loop (quit)

        case _: # In case that the user's choosen option is not exists
            print("Error: Incorrect menu option has been choosen. Please try again.")   # Print error message in case that incorrect menu option has choosen
    # Menu Options End
    input("Press Enter to return to the Main Menu.")    # Prompt the input message each time into the loop for returning to Main Menu
# Loop Menu End