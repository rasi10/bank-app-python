class Customer:
    def __init__(self, id, name, pnr, accounts=[]):
        self.id = id
        self.name = name
        self.pnr = pnr
        self.accounts = accounts
