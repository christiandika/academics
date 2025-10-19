# %%
import os
from datetime import datetime

# Definition of global variables
EXPENSE_DATABASE_FILE = "expense_database.csv"
#EXPENSE_DATABASE_FILE = "test.txt"
VALID_DATE_FORMAT = "%Y-%m-%d"
EXPENSE_CATEGORIES = ("Housing", "Utilities", "Groceries", "Transportation", "Health", "Childcare", "Education", "Dining & Entertainment", "Travel", "Miscellaneous")
NUMBER_OF_EXPENSE_CATEGORIES = len(EXPENSE_CATEGORIES)
CURRENT_YEAR = datetime.now().year
EXPENSE_DESCRIPTION_MAX_LENGTH = 100
CSV_DELIMITER = ","
EXPENSE_TRACKER_COMMANDS = ("Add expense","View expenses","Track budget","Set budget","Exit")
EXPENSES = list() # Initiate the list containing all expenses
BUDGETS = dict() # Initiate the dictionary containing all budgets

# %%
# Menu List of expense categories
def displayCategoriesMenuList():
    categories_list = "##########################################################\n"
    for category in EXPENSE_CATEGORIES:
        categories_list += str(EXPENSE_CATEGORIES.index(category) + 1) + " : " + str(category) + "\n"
    categories_list += "##########################################################\n"
    print(categories_list)

# %%
displayCategoriesMenuList()

# %%
# Run this to play with some test data
test_data = "Date,Category,Amount,Description\n2025-04-05,Housing,682.42,Home insurance premium\n2025-04-06,Transportation,55.82,Gas fill-up for Mary's car\n2025-04-12,Education,37.54,School supplies for Peter\n2025-03-23,Utilities,50.62,Trash collection fee\n2025-04-08,Miscellaneous,50.39,Pet supplies from PetSmart\n2025-01-30,Dining & Entertainment,20.96,Bob and Mary date night\n2025-01-13,Transportation,69.72,Tollway charges\n2025-02-05,Dining & Entertainment,14.24,Bob and Mary date night\n2025-03-21,Childcare,214.12,Kids activity club monthly fee\n2025-04-05,Groceries,49.7,Monthly stock-up from Kroger"
print(test_data)
test_file = open(EXPENSE_DATABASE_FILE, "w")
test_file.write(test_data)
test_file.close()

# %%
# Function to print an expense entry
def printExpenseLine(expense):
    if not isinstance(expense, dict):
        print("ERROR: This object is not an expense:", expense)
        return
    elif set(expense.keys()) != {"date", "category", "amount", "description"}:
        print("ERROR: This object is not an expense:", expense)
        return
    else:
        expense_line = ""
        for i, j in expense.items():
            if str(j) == "":
                print("Expense details are incomplete on this record:", expense)
                return
            else:
                expense_line += str(i) + ": "+ str(j) + "\t"
        print(expense_line)

# Function to diplay all expenses
def viewExpenses():
    for expense in EXPENSES: printExpenseLine(expense)

# %%
# Load expenses from expense database file, or create expense database file if it does not exist
def loadExpenses():
    global EXPENSES
    EXPENSES = list()
    if not os.path.exists(EXPENSE_DATABASE_FILE):
        expense_file = open(EXPENSE_DATABASE_FILE, 'x')
        expense_file.write(f'Date{CSV_DELIMITER}Category{CSV_DELIMITER}Amount{CSV_DELIMITER}Description')
        expense_file.close()
        print("A new expense tracker file was created. You do not have any recorded expense yet.")
    else:
        expense_file = open(EXPENSE_DATABASE_FILE, 'r')
        expense_file_content = expense_file.read()
        expense_list = expense_file_content.split("\n")
        #print(expense_list)
        expense_keys = ['date','category','amount','description']
        i = 0
        for expense_line in expense_list:
            i += 1
            if i == 1: continue # Skip header
            expense_line_split = expense_line.split(CSV_DELIMITER,3)
            expense_dict = dict(zip(expense_keys, expense_line_split))
            #print(expense_dict)
            EXPENSES.append(expense_dict)
            #print(EXPENSES)
        expense_file.close()
        print("Below is the list of all your recorded expenses\n")
        viewExpenses()

# %%
loadExpenses()

# %%
# Funtion to check if an input value is a date in the format YYYY-MM-DD
def isValidDate(date_input):
    try:
        datetime.strptime(date_input, VALID_DATE_FORMAT)
        return True
    except ValueError:
        return False

# Funtion to check if an input value is a date in the format YYYY-MM-DD
def isValidDateCurrentOrPast(date_input):
    try:
        date_obj = datetime.strptime(date_input, VALID_DATE_FORMAT)
        return date_obj.date() <= datetime.now().date()
    except ValueError:
        return False

# Function to check if an input is valid expense date
def isValidExpenseDate():
    expense_date = input("Expense date in format YYYY-MM-DD:")
    while not(isValidDate(expense_date)):
        date = input("You must enter a valid date in this format: YYYY-MM-DD")

# Funtion to check if an input value is either this year or last year
def isValidYearForBudget(year_input):
    try:
        year = int(year_input)
        return (CURRENT_YEAR -1 <= year <= CURRENT_YEAR)
    except ValueError:
        return False

# Funtion to check if an input value is a valid month represented by an integer between 1 and 12
def isValidMonth(month_input):
    try:
        month = int(month_input)
        return (1 <= month <= 12)
    except ValueError:
        return False

# Funtion to check if the expense category number (or category index or categoty option) selected by the user is valid
def isValidCategoryNumber(category_number):
    if (not category_number.isdigit()
        or int(category_number) > NUMBER_OF_EXPENSE_CATEGORIES
        or int(category_number) < 1):
        return False
    return True

# Funtion to check if an amount is a positive number
def isValidAmount(amount_input):
    try:
        amount = float(amount_input)
        if amount > 0: return True
        else: return False
    except ValueError:
        return False

# Funtion to check if the interactive menu option selected by the user is valid
def isValidInteractiveMenuOption(menu_option):
    if (not menu_option.isdigit()
        or int(menu_option) > len(EXPENSE_TRACKER_COMMANDS)
        or int(menu_option) < 1):
        return False
    return True

# %%
# Function to capture the expense date user input: the date must be today on in the past, in the format YYYY-MM-DD
def inputExpenseDate():
    date = input("Expense date in format YYYY-MM-DD:")
    while not(isValidDateCurrentOrPast(date)):
        date = input("You must enter a valid current or past date in this format: YYYY-MM-DD")
    return datetime.strptime(date, VALID_DATE_FORMAT).strftime(VALID_DATE_FORMAT)

# %%
# Function to capture the expense category user input
def inputExpenseCategory():
    displayCategoriesMenuList()
    category_number = input(f"Select the category by entering a digit between 1 and {NUMBER_OF_EXPENSE_CATEGORIES}:")    
    while (not isValidCategoryNumber(category_number)):
        category_number = input(f"You must enter an integer between 1 and {NUMBER_OF_EXPENSE_CATEGORIES}")
    category = EXPENSE_CATEGORIES[int(category_number) - 1]
    print("Category:",category)
    return category

# %%
# Function to capture the expense year user input - restricted to current year or last year
def inputRecentExpenseYear():
    year = input(f"Enter the year, either {CURRENT_YEAR} or {CURRENT_YEAR-1}:")
    while not(isValidYearForBudget(year)):
        year = input(f"Enter a valid year, either {CURRENT_YEAR} or {CURRENT_YEAR-1}:")
    return year

# %%
# Function to capture the month user input
def inputMonthNumber():
    month_number = input("Enter the month represented by a number between 1 and 12:")
    while not(isValidMonth(month_number)):
        month_number = input("Enter a valid month represented by a digit between 1 and 12:")
    return month_number

# %%
# Function to capture the amount user input
def inputAmount():
    amount = input("Amount:")
    while not(isValidAmount(amount)):
        amount = input("You must enter a valid number that is greater than 0:")
    return round(float(amount), 2)

# %%
# Function to capture the expense description user input
def inputExpenseDescription():
    description = input(f"Description ({EXPENSE_DESCRIPTION_MAX_LENGTH} characters or less):")
    while len(description) > EXPENSE_DESCRIPTION_MAX_LENGTH:
        description = input(f"Enter a description that has {EXPENSE_DESCRIPTION_MAX_LENGTH} characters or less:")
    return description

# %%
# Function to save an expense in the database (expense file)
def saveExpenseInDb(date, category, amount, description):
    expense_file = open(EXPENSE_DATABASE_FILE, 'a')
    expense_file.write(f'\n{date}{CSV_DELIMITER}{category}{CSV_DELIMITER}{amount}{CSV_DELIMITER}{description}')
    expense_file.close()

# %%
# Function to add an expense
# This function automatically saves the expense in the file. The user doesn't have to call anoher function to save the expenses, which they may forget to do. So this is a better solution
def addExpense():
    
    date = inputExpenseDate()
    category = inputExpenseCategory()
    amount = inputAmount()
    description = inputExpenseDescription()
    
    # Save expense in database (expense file)
    saveExpenseInDb(date, category, amount, description)
    
    #Create expense dictionary object
    expense = {
        "date": date,
        "category": category,
        "amount": round(float(amount), 2),
        "description": description
    }    
    print("Expense added:", expense)
    
    #Add expense to list of expenses
    EXPENSES.append(expense)

# %%
# Function to enable the user to set the budget for a month for either this year or last year only (for analytics purposes)
def setMonthBudget():
    print("Budget setting...")
    year = inputRecentExpenseYear()
    month_number = inputMonthNumber()
    month = datetime(CURRENT_YEAR, int(month_number), 1).strftime('%b')
    budget = inputAmount()
    
    # Record the budget
    if year not in BUDGETS: BUDGETS[year] = dict()
    BUDGETS[year][month] = budget
    print(f"Budget set:\t{year}\t{month}\t{budget}")

# %%
def getTotalExpense(year, month_number):
    # Check that the year and month are valid
    if not isValidYearForBudget(year):
        print(f"Try again. Enter a valid year, either {CURRENT_YEAR} or {CURRENT_YEAR-1}.")
        return
    if not isValidMonth(month_number):
        print("Try again. Enter a valid month represented by a number between 1 and 12.")
        return

    total_expenses = 0
    for expense in EXPENSES:
        #capture date elements
        expense_date_string = expense["date"]
        expense_date = datetime.strptime(expense_date_string, VALID_DATE_FORMAT)
        expense_year = expense_date.year
        expense_month = expense_date.month

        #check if this expense was made in the input year and month
        if(expense_year == year and expense_month == month_number):
            total_expenses += float(expense["amount"])
    return round(total_expenses,2)

# %%
def trackExpenses():    
    year_string = inputRecentExpenseYear()
    year_number = int(year_string)
    month_number = int(inputMonthNumber())    
    month_3char = datetime(CURRENT_YEAR, month_number, 1).strftime('%b')
    
    if year_string not in BUDGETS or month_3char not in BUDGETS[year_string]:
        print(f"No budget was defined for {month_3char} {year}. You must first set that budget by using the function setMonthBudget().")
        return
    
    budget = BUDGETS[year_string][month_3char]
    total_expenses = getTotalExpense(year_number, month_number)
    remaining_balance = round(budget - total_expenses,2)

    print("Period:", year_string, month_3char)
    print ("Budget:", budget)
    print ("Total Expenses:", total_expenses)

    if remaining_balance > 0: print (f"Your remaining balance is ${remaining_balance}")
    elif remaining_balance < 0: print (f"WARNING!!! You have exceeded your budget by ${remaining_balance}")
    elif remaining_balance == 0: print ("You have exhausted your budget. Your remaining balance is $0.00")

# %%
# Menu List of expense tracker commands
def displayExpenseTrackerCommands():
    commands_display = f"What would you like to do next?"
    for command in EXPENSE_TRACKER_COMMANDS:
        commands_display += "\n" + str(EXPENSE_TRACKER_COMMANDS.index(command) + 1) + " : " + str(command)
    print(commands_display)

# %%
def interactiveMenu():
    while True:
        displayExpenseTrackerCommands()
        menu_option = input(f"Choose between option 1 and {len(EXPENSE_TRACKER_COMMANDS)}:")
        while not isValidInteractiveMenuOption(menu_option):
            menu_option = input(f"You must enter a digit between option 1 and {len(EXPENSE_TRACKER_COMMANDS)}:")
        menu_option = int(menu_option)
        match menu_option:
            # addExpense() automatically saves the expense in the file. The user does not ave to call anoher function to save the expenses, which they may forget to do
            case 1: addExpense()        
            case 2: viewExpenses()
            case 3: trackExpenses()
            case 4: setMonthBudget()
            case 5:
                print("Bye!")
                exit()

# %%
interactiveMenu()



