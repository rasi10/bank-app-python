from classes.Account import Account
from classes.Bank import Bank
from classes.Customer import Customer


def main():
    b1 = Bank('Nordea')
    # The file location is set to be run with the script file
    # customers = b1._load('src/bank_registers/bank.txt')    

    # customers = b1.get_customers('src/bank_registers/bank.txt')
    # print(customers)

    # customer = b1.get_customer('src/bank_registers/bank.txt', '199911114')
    # print(repr(customer))

    '''
    b1.add_customer('src/bank_registers/bank.txt', 'Name00', '199911114')
    b1.add_customer('src/bank_registers/bank.txt', 'Name11', '199911115')
    b1.add_customer('src/bank_registers/bank.txt', 'Name22', '199911116')
    b1.add_customer('src/bank_registers/bank.txt', 'Name33', '199911117')
    b1.add_customer('src/bank_registers/bank.txt', 'Name44', '199911118')

    
    
    result = b1.get_customer('src/bank_registers/bank.txt', '199911112')
    print(result)
    '''

    #print(b1.add_customer('src/bank_registers/bank.txt', 'Name55', '199911123'))

    '''
    result = b1.remove_customer('src/bank_registers/bank.txt', '199911115')
    print(result)
    '''
    # print(b1.change_customer_name('src/bank_registers/bank.txt', 'janedoe2', '199911117'))
    
    # print(b1.add_account('src/bank_registers/bank.txt', '199911117'))
    
    # print(b1.get_account('src/bank_registers/bank.txt', '199911116','c0fac42d-62d3'))
    # print(b1.deposit('src/bank_registers/bank.txt', '199911116','62fed90e-62e2', 20.0))
    # print(b1.withdraw('src/bank_registers/bank.txt', '199911116','62fed90e-62e2', 20.0))
    
    print(b1.close_account('src/bank_registers/bank.txt', '199911117','c0fac41f-62d3'))
    #print(b1.close_account('src/bank_registers/bank.txt', '199911118', 'c0fac431-62d3'))

if __name__ == '__main__':
    main()

