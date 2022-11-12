from .Customer import Customer

class Account:
    def __init__(self, account_number, balance, account_type='debit account'):
        self.balance = balance
        self.account_number = account_number
        self.account_type = account_type

    def __str__(self):        
        return f'Number: {self.account_number}|Type: {self.account_type}|Balance: {self.balance} #'
