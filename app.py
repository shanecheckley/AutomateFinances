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

def menu():
    connection = database.connect()
    database.create_tables(connection)
    
    #look up ":=", does this mean: should be equal to?
    while (user_input := input(MENU_PROMPT)) != "5":
        print(user_input)
