class Bank:
    def __init__(self, name):        
        self.name = name

    def _load(self, input_file):
        f = open(input_file,'r')
        print(f.read())
        
    def get_customers():
        pass

    def add_customer(name, pnr):
        pass

    def get_customer(pnr):
        pass
    
    def change_customer_name(name, pnr):
        pass
    
    def remove_customer(pnr):
        pass
    
    def add_account(pnr):
        pass
    
    def get_account(pnr, account_id):
        pass

    def deposit(pnr, account_id, amount):
        pass

    def withdraw(pnr, account_id, amount):
        pass

    def close_account(pnr, account_id):
        pass
