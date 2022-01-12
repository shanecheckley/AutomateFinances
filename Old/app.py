from sqlite3.dbapi2 import connect
import database

MENU_PROMPT = """
Please choose one if these options:

1) Add a new transaction
2) See all transactions
3) Find a transaction by name(description)
4) Find total $ of category
5) Exit

Your selection:
"""

# main menu
def menu():
    connection = database.connect()
    database.create_tables(connection)
    get_input(connection)


# ***HELPER FUNCTIONS***

def get_input(connection):   
    # ":=" gives a new variable (left side) a value (right side) within a statement
    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            get_new_transactions(connection)
        elif user_input == "2":
            see_all_transactions(connection)
        elif user_input == "3":
            find_by_description(connection)
        elif user_input == "4":
            sum_of_category(connection)
        else:
            print("****Invalid input, please try again!*****")

def get_new_transactions(connection):
    date = input("Enter date: ")
    description = input("Enter description: ")
    transaction_type = input("Enter transaction type (withdrawal, deposit, transfer): ")
    # casting input to int... look into this more
    amount = int(input("Enter amount: "))
    debit_or_credit = input("Debit or credit?: ")
    purchase_method = input("Enter purchase method: ")
    category = input("Enter category: ")

    database.add_transaction(connection, date, description, transaction_type, amount, debit_or_credit, purchase_method, category)

def see_all_transactions(connection):
    transactions = database.get_all_transactions(connection)

    for transaction in transactions:
        print(transaction)

def find_by_description(connecition):
    user_input = input("Enter description: ")
    description = database.get_transactions_by_description(connecition, user_input)
    print(description)

def sum_of_category(connection):
    category = input("Enter category: ")
    amount = database.get_category_total(connection, category)
    print(amount)
