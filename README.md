
![Logo](https://png.pngtree.com/png-vector/20220910/ourmid/pngtree-budgeting-icon-png-image_6145091.png)


# Budget Manager Project

Manage your budget easily by adding income/expense transactions.


## Features

- Transactions control (incomes/expenses)
- Current Balance visibility
- Transactions history
- "Easy-to-understand" code (comments everywhere)


## Code Explainations
### Structure Method Used

The method used in the code below creating a dictionary with a transactions list, including starting balance, transaction type, amount and description:
```python
budget_data = {
"balance": 500,
"transactions": [
{"type": "income", "amount": 1000, "description": "Salary"},
{"type": "expense", "amount": 500, "description": "Groceries"}
]
}
```
Each transaction will be stored separately in a new line *(see example below)*:

```{"type": "expense", "amount": 500, "description": "Groceries"}```

The user's balance value will be overrited in the main ```budget_manager.py``` file after each transaction.

### Main Menu
The menu contains loop with match-cases, the user will be asked to press **Enter** in order to return to the menu again after the function completion.

In case the user's input is incorrect or not exists in the menu - error message will be printed.
### Functions File
There is ```transactions.py``` file with all menu match cases functions which including most of code. The menu handler exists in the file as well.


## Files Included

[```budget_manager.py```](https://github.com/desmondcoacher/budget_manager/blob/main/budget_manager.py) *(Main File)*

[```transactions.py```](https://github.com/desmondcoacher/budget_manager/blob/main/transactions.py) *(Functions File)*


## Licensing

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://github.com/desmondcoacher/budget_manager/blob/main/LICENSE)



## Authors

- [@desmondcoacher](https://github.com/desmondcoacher)


## Feedback

If you have any feedback, feel free to contact me: desmond.c@campus.technion.ac.il

