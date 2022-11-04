from .Customer import Customer
class Account:
    def __init__(self, x):
        self.x = x

    def print_account(self):
        print('hello, Account')

    def test(self, c):        
        c.print_customer()