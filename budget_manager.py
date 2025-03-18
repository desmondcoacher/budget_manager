# budget_data = {
#  "balance": 500,
#  "transactions": [
#  {"type": "income", "amount": 1000, "description": "Salary"},
#  {"type": "expense", "amount": 500, "description": "Groceries"}
#  ]
# }

while True:

    print("\n" + "*" * 25)
    print("Welcome to Budget Manager")
    print("*" * 25 + "\n")

    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Show Transaction History")
    print("5. Exit\n")
    
    userChoise = input("Enter menu option: ")

    match userChoise:

        case "1":
            print("Menu option 1 has been choosen.")
            pass

        case "2":
            print("Menu option 2 has been choosen.")
            pass

        case "3":
            print("Menu option 3 has been choosen.")
            pass

        case "4":
            print("Menu option 4 has been choosen.")
            pass

        case "5":
            print("Menu option 5 has been choosen.")
            break

        case _:
            print("Error: Incorrect menu option has been choosen. Please try again.\n")