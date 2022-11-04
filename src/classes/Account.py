from .Customer import Customer
import uuid
class Account:
    def __init__(self, balance):
        new_account_number = str(uuid.uuid1())
        
        self.balance = balance
        self.account_number = new_account_number[0:11]
        self.account_name = 'debit account'
            