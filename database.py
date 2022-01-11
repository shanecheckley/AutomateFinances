import sqlite3

# SQL Queries
CREATE_TRANSACTION_TABLE = "CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY, date TEXT, description TEXT, transaction_type TEXT, amount INTEGER, debit_or_credit TEXT, purchase_method TEXT, category TEXT);"
INSERT_TRANSACTION = "INSERT INTO transactions (date, description, transaction_type, amount, debit_or_credit, purchase_method, category) VALUES (?, ?, ?, ?, ?, ?, ?);"
GET_ALL_TRANSACTIONS = "SELECT * FROM transactions;"
GET_TRANSACTIONS_BY_DESCRIPTION = "SELECT * FROM transactions WHERE description = ?;"
GET_CATEGORY_TOTAL = """
SELECT SUM(category) 
FROM transactions
WHERE category = ?
"""

# connect to the data file
def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_TRANSACTION_TABLE)

def add_transaction(connection, date, description, transaction_type, amount, debit_or_credit, purchase_method, category):
    with connection:
        # execution that requires values: values must be tuples
        connection.execute(INSERT_TRANSACTION, (date, description, transaction_type, amount, debit_or_credit, purchase_method, category))

def check_if_added(connection):
    pass

def get_all_transactions(connection):
    with connection:
        return connection.execute(GET_ALL_TRANSACTIONS).fetchall()

def get_transactions_by_description(connection, description):
    with connection:
        # execution that requires values: values must be tuples
        return connection.execute(GET_TRANSACTIONS_BY_DESCRIPTION, (description,))

def get_category_total(connection, category):
    with connection:
        # execution that requires values: values must be tuples
        return connection.execute(GET_CATEGORY_TOTAL, (category,))