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


if __name__ == '__main__':
    main()
