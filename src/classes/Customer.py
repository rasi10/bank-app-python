class Customer:
    def __init__(self, id, name, pnr, accounts=[]):
        self.id = id
        self.name = name
        self.pnr = pnr
        self.accounts = accounts

    def __repr__(self):
        accounts_as_string = ''
        for account in self.accounts:
            accounts_as_string += str(account)
        return f'Name: {self.name} - PNR: {self.pnr} - Accounts: {accounts_as_string}'

    def __str__(self):
        accounts_as_string = ''
        for account in self.accounts:
            accounts_as_string += str(account)
        return f'ID: {self.id} - Name: {self.name} - PNR: {self.pnr} - Accounts: {accounts_as_string}'
