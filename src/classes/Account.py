from .Customer import Customer


class Account:
    def __init__(self, account_number, balance, account_name='debit account'):
        self.balance = balance
        self.account_number = account_number
        self.account_name = account_name
