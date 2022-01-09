class Transaction:
    # Contrstuctor for all transactions that are not purchases (without category)
    def __init__(self, date, description, transaction_type, amount):
        self.date = date
        self.description = description
        self.transaction_type = transaction_type
        self.amount = amount
        category = none
    
    # Constructor for purchase transactions (without category)
    def __init__(self, date, description, transaction_type, amount, debit_or_credit, purchase_method):
        self.date = date
        self.description = description
        self.transaction_type = transaction_type
        self.amount = amount
        self.debit_or_credit = debit_or_credit
        self.purchase_method = purchase_method
        category = none
    
    # Contrstuctor for all transactions that are not purchases
    def __init__(self, date, description, transaction_type, amount, category):
        self.date = date
        self.description = description
        self.transaction_type = transaction_type
        self.amount = amount
        self.category = category
    
    # Constructor for purchase transactions
    def __init__(self, date, description, transaction_type, amount, debit_or_credit ,purchase_method, category):
        self.date = date
        self.description = description
        self.transaction_type = transaction_type
        self.amount = amount
        self.debit_or_credit = debit_or_credit
        self.purchase_method = purchase_method
        self.category = category
    
    def set_date(self, date):
        self.date = date
    
    def set_description(self, description):
        self.description = description
    
    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type

    def set_amount(self, amount):
        self.amount = amount
    
    def set_debit_or_credit(self, debit_or_credit):
        self.debit_or_credit = debit_or_credit
    
    def set_purchase_method(self, purchase_method):
        self.purchase_method = purchase_method
    
    def set_category(self, category):
        self.category = category

    def get_date():
        return date
    
    def get_description():
        return description
    
    def get_transaction_type():
        return transaction_type
    
    def get_amount():
        return amount
    
    def get_debit_or_credit():
        return debit_or_credit
    
    def get_purchase_method():
        return purchase_method
    
    def get_category():
        return category
    
    # change this later to better represent a repr function
    def __repr__(self):
        return """{}
        {}
        {}
        {}""".format(self.date, self.description, self.transaction_type, self.amount)
    
    # def format_type(transaction_type): 
    
    # def find_type(transaction_type):