import sqlite3

# SQL Queries
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY, date TEXT, description TEXT, transaction_type TEXT, amount INTEGER, debit_or_credit TEXT, purchase_method TEXT, category TEXT);"
INSERT = "INSERT INTO transactions (date, description, transaction_type, amount, debit_or_credit, purchase_method, category) VALUES (?, ?, ?, ?, ?, ?, ?);"
GET_ALL = "SELECT * FROM transactions;"
GET_BY_DESCRIPTION = "SELECT * FROM transactions WHERE description = ?;"
GET_CATEGORY_SUM = "SELECT SUM(amount) FROM transactions WHERE category = ?"

# connect database to the data file
def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE)

def add_transaction(connection, date, description, transaction_type, amount, debit_or_credit, purchase_method, category):
    with connection:
        # execution that requires values: values must be tuples
        connection.execute(INSERT, (date, description, transaction_type, amount, debit_or_credit, purchase_method, category))

def check_if_added(connection):
    pass

def get_all_transactions(connection):
    with connection:
        return connection.execute(GET_ALL).fetchall()

def get_transactions_by_description(connection, description):
    with connection:
        # execution that requires values: values must be tuples
        return connection.execute(GET_BY_DESCRIPTION, (description,)).fetchone()

def get_category_total(connection, category):
    with connection:
        # execution that requires values: values must be tuples
        return connection.execute(GET_CATEGORY_SUM, (category,)).fetchone()