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
            if (len(accounts) == 1):                
                account = Account(line.split(':')[3],line.split(':')[5] )
                customer_accounts.append(account)
                customer = Customer(line.split(':')[0], line.split(':')[1], line.split(':')[2], customer_accounts)
                all_customers.append(customer)
            elif len(accounts) > 1:                               
                account = Account(line.split(':')[3],line.split(':')[5].split('#')[0])
                customer_accounts.append(account)              
                for i in range(1, len(accounts)):                    
                    account = Account(accounts[i].split(':')[0],accounts[i].split(':')[2] )
                    customer_accounts.append(account)
                customer = Customer(line.split(':')[0], line.split(':')[1], line.split(':')[2], customer_accounts)
                all_customers.append(customer)
            customer_accounts = []
        return all_customers
 
  
    def get_customers(self, input_file): 
        list_of_customers = self._load(input_file)
        customers = []       
        for customer in list_of_customers:            
            customers.append(f'Name: {customer.name} - PNumber:{customer.pnr}')
        return customers    

    
    def add_customer(self, input_file, name, pnr):
        list_of_customers = self._load(input_file)        
        duplicate_checker = True       
        while duplicate_checker == True:               
            new_customer_id = str(uuid.uuid1())[0:8]            
            for customer in list_of_customers:                
                while customer.id == new_customer_id:                    
                    new_customer_id = str(uuid.uuid1())[0:8]
            duplicate_checker = False        
        for customer in list_of_customers:
            if customer.pnr == pnr:
                return False        
        new_customer = Customer(new_customer_id,name, pnr)
        account = Account(str(uuid.uuid1())[0:13], 0.0)        
        with open(input_file, 'a') as file:
            file.write(f'{new_customer.id}:{new_customer.name}:{new_customer.pnr}:{account.account_number}:{account.account_type}:{account.balance}\n')
        return True
 
    def get_customer(self, input_file, pnr):
        list_of_customers = self._load(input_file)
        for customer in list_of_customers:
            if customer.pnr == pnr:
                return customer
        return 'User not found!'  
    
   
    def change_customer_name(self, input_file, name, pnr):
        list_of_customers = self._load(input_file)        
        for index, customer in enumerate(list_of_customers):
            if customer.pnr == pnr:
                list_of_customers[index].name = name
                with open(input_file, 'w') as file:
                    for customer in list_of_customers:
                        accounts = customer.accounts
                        account_string = ''
                        for acc in accounts:
                            account_string += f'{acc.account_number}:{acc.account_type}:{acc.balance.strip()}#'
                        file.write(f'{customer.id}:{customer.name}:{customer.pnr}:{account_string[:-1]}\n')                
                return True
        return False

    def remove_customer(self, input_file, pnr):            
        list_of_customers = self._load(input_file)        
        result_list = []
        saldo = 0 
        for customer in list_of_customers:
            if customer.pnr == pnr:
                accounts = customer.accounts
                for acc in accounts:
                    result_list.append(str(acc)[1:-1])
                    saldo += float(acc.balance)
                list_of_customers.remove(customer)
               
                with open(input_file, 'w') as file:
                    for customer in list_of_customers:
                        accounts = customer.accounts
                        account_string = ''
                        for acc in accounts:
                            account_string += f'{acc.account_number}:{acc.account_type}:{acc.balance.strip()}#'
                        file.write(f'{customer.id}:{customer.name}:{customer.pnr}:{account_string[:-1]}\n')
                
                return result_list, saldo
        return False
    
    
    def add_account(self,input_file, pnr):
        list_of_customers = self._load(input_file)
        for index, customer in enumerate(list_of_customers):
            if customer.pnr == pnr:
                account = Account(str(uuid.uuid1())[0:13], 0.0)
                list_of_customers[index].accounts.append(account)                
                with open(input_file, 'w') as file:
                    for customer in list_of_customers:
                        accounts = customer.accounts
                        account_string = ''
                        for acc in accounts:
                            account_string += f'{acc.account_number}:{acc.account_type}:{str(acc.balance).strip()}#'
                        file.write(f'{customer.id}:{customer.name}:{customer.pnr}:{account_string[:-1]}\n')                
                return account.account_number
        return -1
       
    def get_account(self, input_file, pnr, account_id):
        list_of_customers = self._load(input_file)
        for index, customer in enumerate(list_of_customers):
            if customer.pnr == pnr:                
                accounts = customer.accounts                        
                for acc in accounts:
                    if acc.account_number == account_id:
                        return repr(acc)                
        return 'Account not found'
    
    
 
    def deposit(self, input_file, pnr, account_id, amount):
        list_of_customers = self._load(input_file)
        for index, customer in enumerate(list_of_customers):
            if customer.pnr == pnr:              
                accounts = customer.accounts                        
                for i, acc in enumerate(accounts):
                    if acc.account_number == account_id:                        
                        value = float(accounts[i].balance) + amount
                        accounts[i].balance = float(value)                        
            with open(input_file, 'w') as file:
                for customer in list_of_customers:
                    accounts = customer.accounts
                    account_string = ''
                    for acc in accounts:
                        account_string += f'{acc.account_number}:{acc.account_type}:{str(acc.balance).strip()}#'
                    file.write(f'{customer.id}:{customer.name}:{customer.pnr}:{account_string[:-1]}\n')    
            return True
        return 'Account not found'
   
  
    def withdraw(self, input_file, pnr, account_id, amount):
        list_of_customers = self._load(input_file)
        for index, customer in enumerate(list_of_customers):
            if customer.pnr == pnr:              
                accounts = customer.accounts                        
                for i, acc in enumerate(accounts):
                    if acc.account_number == account_id:                        
                        value = float(accounts[i].balance) - amount
                        if value < 0:
                            print('You do not have enough saldo to perform this operation')
                            return False
                        accounts[i].balance = float(value)                        
            with open(input_file, 'w') as file:
                for customer in list_of_customers:
                    accounts = customer.accounts
                    account_string = ''
                    for acc in accounts:
                        account_string += f'{acc.account_number}:{acc.account_type}:{str(acc.balance).strip()}#'
                    file.write(f'{customer.id}:{customer.name}:{customer.pnr}:{account_string[:-1]}\n')    
            return True
        return 'Account not found'


    def close_account(self, input_file, pnr, account_id):
        list_of_customers = self._load(input_file)
        validator = False
        saldo = 0.0
        for index, customer in enumerate(list_of_customers):            
            if pnr == list_of_customers[index].pnr:                
                accounts = customer.accounts                        
                for acc in accounts:                     
                    if acc.account_number == account_id:
                        if len(accounts) > 1:     
                            saldo = acc.balance                    
                            list_of_customers[index].accounts.remove(acc)                            
                            validator = True
                        else:
                            validator = False
        
        if validator == True:
            with open(input_file, 'w') as file:
                for customer in list_of_customers:
                    accounts = customer.accounts
                    account_string = ''
                    for acc in accounts:
                        account_string += f'{acc.account_number}:{acc.account_type}:{str(acc.balance).strip()}#'
                    file.write(f'{customer.id}:{customer.name}:{customer.pnr}:{account_string[:-1]}\n')    
            return True, f'Saldo: {saldo}'
        else:
            return False              
                        
                        


