# 🧾 Personal Expense Tracker

## Overview
The **Personal Expense Tracker** is a Python-based console application designed to help users manage their daily expenses, categorize spending, and track budgets effectively.  
It supports saving and loading expense data from a CSV file, allowing users to maintain a persistent record across sessions.

> **Python version:** The code was executed and tested with **Python 3.12.10**.

---

## Objectives
This project aims to:
1. Enable users to **log daily expenses** with date, category, amount, and description.
2. Allow categorization of expenses (e.g., Food, Travel, Groceries, etc.).
3. Support **budget tracking** against user-defined monthly limits.
4. Implement **file handling** for saving and loading expenses.
5. Provide a simple **interactive, menu-driven interface**.

---

## Features

### 1. Add Expense
Users can add a new expense by entering:
- **Date:** Must be in `YYYY-MM-DD` format (current or past date).
- **Category:** Selected from a predefined list of categories (e.g., Housing, Transportation, Health, etc.).
- **Amount:** Must be a positive number.
- **Description:** A short text (max 100 characters).

Each expense is saved automatically into the local CSV file (`expense_database.csv`) and stored in memory as a dictionary:
```python
{'date': '2025-04-06', 'category': 'Transportation', 'amount': 55.82, 'description': 'Gas fill-up for car'}
```

---

### 2. View Expenses
Displays all recorded expenses from memory or file, formatted with clear field labels:
```
date: 2025-04-06  category: Transportation  amount: 55.82  description: Gas fill-up for car
```
Incomplete or invalid entries are automatically skipped or flagged.

---

### 3. Set Monthly Budget
Users can set a **monthly budget** for the current or previous year.  
Input required:
- Year (`YYYY`)
- Month (numeric 1–12)
- Budget amount

Budgets are stored in a dictionary:
```python
BUDGETS = {
    "2025": {"Apr": 1500.00, "May": 1200.00}
}
```

---

### 4. Track Budget
Calculates the **total expenses** for a given month and compares them with the defined budget:
- Displays total expenses and remaining balance.
- Warns the user if the budget is exceeded.

Example output:
```
Period: 2025 Apr
Budget: 1500.0
Total Expenses: 1472.50
Your remaining balance is $27.50
```

---

### 5. Save and Load Expenses
- **Load:** Automatically loads previously saved expenses from `expense_database.csv` at program start.
- **Save:** Each expense is written to file immediately after creation, ensuring no data loss.

CSV structure:
```
Date,Category,Amount,Description
2025-04-05,Housing,682.42,Home insurance premium
2025-04-06,Transportation,55.82,Gas fill-up
```

---

### 6. Interactive Menu
A text-based menu lets users navigate the application:
```
What would you like to do next?
1 : Add expense
2 : View expenses
3 : Track budget
4 : Set budget
5 : Exit
```

---

## Program Structure

### Main Modules and Functions
| Function | Purpose |
|-----------|----------|
| `displayCategoriesMenuList()` | Shows all available expense categories. |
| `loadExpenses()` | Loads existing expenses from file (creates file if missing). |
| `addExpense()` | Adds a new expense and writes to CSV. |
| `viewExpenses()` | Displays all recorded expenses. |
| `setMonthBudget()` | Allows setting a monthly budget. |
| `trackExpenses()` | Compares expenses vs. budget and displays remaining balance. |
| `interactiveMenu()` | Controls the menu-driven interface. |

---

## Files
| File | Description |
|------|--------------|
| `personal_expense_tracker.py` | Main Python script containing the implementation. |
| `expense_database.csv` | CSV file for persistent storage of expenses. |
| `Project 1 - Personal Expense Tracker.docx` | Exercise description and project requirements. |

---

## How to Run

### 1. Clone or download the repository.
```bash
git clone <repo_url>
cd personal-expense-tracker
```

### 2. Run the program using Python 3.12.10.
```bash
python personal_expense_tracker.py
```

### 3. Follow the on-screen menu to interact with the tracker.

---

## Example Session
```
##########################################################
1 : Housing
2 : Utilities
3 : Groceries
4 : Transportation
5 : Health
...
##########################################################
What would you like to do next?
1 : Add expense
2 : View expenses
3 : Track budget
4 : Set budget
5 : Exit
```

---

## Future Enhancements
- Add visualization (monthly summaries, pie charts).
- Support deletion or editing of expenses.
- Enable multiple users or profiles.
- Export reports to Excel or PDF.

---

## Author
**Christian Dika**  
Project: *Personal Expense Tracker*  
Language: *Python 3.12.10*  
Date: *April 2025*
