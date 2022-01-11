from sqlite3.dbapi2 import connect
import database

MENU_PROMPT = """
Please choose one if these options:

1) Add a new transaction
2) See all transactions
3) Find a transactio by name(description)
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
            date = input("Enter date: ")
            description = input("Enter description: ")
            transaction_type = input("Enter transaction type (withdrawal, deposit, transfer): ")
            # casting input to int... look into this more
            amount = int(input("Enter amount: "))
            debit_or_credit = input("Debit or credit?: ")
            purchase_method = input("Enter purchase method: ")
            category = input("Enter category: ")

            database.add_transaction(connection, date, description, transaction_type, amount, debit_or_credit, purchase_method, category)
        elif user_input == "2":
            transactions = database.get_all_transactions(connection)

            for transaction in transactions:
                print(transaction)
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("****Invalid input, please try again!*****")
