import uuid
from .Customer import Customer
from .Account import Account

class Bank:
    def __init__(self, customers):        
        self.customers = customers
  
    def _load(self, input_file):
        all_customers = []        
        f = open(input_file)
        lines = f.readlines()
        f.close()
        customer_accounts = []
        for line in lines:            
            accounts = line.split('#')
            print(accounts)
            if (len(accounts) == 1):                
                account = Account(line.split(':')[3],line.split(':')[4] )
                customer_accounts.append(account)
                customer = Customer(line.split(':')[0], line.split(':')[1], line.split(':')[2], customer_accounts)
                all_customers.append(customer)
        return all_customers
 
    ''' 
    def get_customers(self, input_file): 
        list_of_customers = self._load(input_file)
        customers = []       
        for customer in list_of_customers:
            c = customer.split(':')
            customers.append(f'Name: {c[1]} - PNumber:{c[2]}')
        return customers    

    def get_customer(self, input_file, pnr):
        list_of_customers = self._load(input_file)
        for customer in list_of_customers:
            c = customer.split(':')
            if pnr == c[2]:
                return customer
        return 'User not found!'
  
    
    def add_customer(name, pnr):
        # new_account_number = str(uuid.uuid1())
        pass


    
    def change_customer_name(self, input_file, name, pnr):
        list_of_customers = self._load(input_file)
        operation_result = False
        index_of_customer = 0
        for i, customer in enumerate(list_of_customers):
            c = customer.split(':')
            if pnr == c[2]:
                operation_result = True
                index_of_customer = i

        if operation_result == True:
            temp = list_of_customers[index_of_customer].split(':')
            temp[1] = name
            list_of_customers[index_of_customer] = str(temp)
            print(list_of_customers)
            with open(input_file, 'w') as fp:                       
                fp.write(list_of_customers)
            fp.close()
            return True
        else:
            print(list_of_customers)
            return False
    
    def remove_customer(pnr):
        pass
    
    def add_account(pnr):
        pass
    
    def get_account(self, input_file, pnr, account_id):
        pass

    def deposit(pnr, account_id, amount):
        pass

    def withdraw(pnr, account_id, amount):
        pass

    def close_account(pnr, account_id):
        pass
    '''