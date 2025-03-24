
![Logo](https://png.pngtree.com/png-vector/20220910/ourmid/pngtree-budgeting-icon-png-image_6145091.png)


# Budget Manager Project

Manage your budget easily by adding income/expense transactions.


## Features

- Track income and expenses effortlessly
- View real-time balance updates
- Maintain a transaction history
- Simple and well-commented code for easy understanding


## Code Explaination
### Data Structure

The program maintains a dictionary that stores the user's balance and a list of transactions. Each transaction includes details like type (income/expense), amount, and description:
```python
transactions_database = {"balance": 0, "transactions": []}
```
Each transaction will be stored separately in a new line *(see example below)*:<br>
```{"type": "expense", "amount": 500, "description": "Groceries"}```<br><br>
The user's balance value will be overrited in the main ```budget_manager.py``` file after each transaction.

### Main Menu
The main menu operates within a loop and uses a match-case structure for handling user choices. After executing a function, the program waits for the user to press Enter to return to the main menu.

**1.** Add Income<br>
**2.** Add Expense<br>
**3.** Show Balance<br>
**4.** Show Transaction History<br>
**5.** Exit<br><br>
Enter menu option:<br><br>
If an invalid option is entered, an error message is displayed.
### Functions File
There is ```transactions.py``` file with all menu match cases functions which including most of code. The menu handler exists in the file as well.

### Functionality Breakdown
All main functionalities are housed in the transactions.py file, which contains:
- The menu handler
- Functions for handling transactions
- Display functions for balance and transaction history<br>
This separation makes the code modular and easier to maintain.

## Project Files

[```budget_manager.py```](https://github.com/desmondcoacher/budget_manager/blob/main/budget_manager.py) *(Main File)*

[```transactions.py```](https://github.com/desmondcoacher/budget_manager/blob/main/transactions.py) *(Functions File)*


## License

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://github.com/desmondcoacher/budget_manager/blob/main/LICENSE)



## Author

- [@desmondcoacher](https://github.com/desmondcoacher)


## Feedback

If you have any feedback, feel free to contact me: desmond.c@campus.technion.ac.il

