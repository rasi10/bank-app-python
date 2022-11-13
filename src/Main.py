from classes.Account import Account
from classes.Bank import Bank
from classes.Customer import Customer


def main():
    b1 = Bank('Nordea')

    ''' Add a couple of customers
    print(b1.add_customer('src/bank_registers/bank.txt', 'Name11', '199911111'))
    print(b1.add_customer('src/bank_registers/bank.txt', 'Name12', '199911112'))
    print(b1.add_customer('src/bank_registers/bank.txt', 'Name13', '199911113'))
    print(b1.add_customer('src/bank_registers/bank.txt', 'Name14', '199911114'))
    print(b1.add_customer('src/bank_registers/bank.txt', 'Name15', '199911115'))
    '''

    ''' Show that you can not add a new customer with the same pnumber
    print(b1.add_customer('src/bank_registers/bank.txt', 'Name33', '199911111'))
    '''

    ''' Show that get_customers() works
    print(b1.get_customers('src/bank_registers/bank.txt'))
    '''

    ''' Show that get_customer() works
    print(b1.get_customer('src/bank_registers/bank.txt', '199911111'))
    '''

    ''' Show that you can not add a new customer with the same pnumber
    print(b1.add_customer('src/bank_registers/bank.txt', 'Name33', '199911111'))
    '''

    ''' Show that you can not add a new customer with a different pnumber
    print(b1.add_customer('src/bank_registers/bank.txt', 'Name16', '199911116'))
    '''

    ''' Show that the method remove_customer() works
    print(b1.remove_customer('src/bank_registers/bank.txt', '199911116'))
    '''

    ''' Show that the method change_customer_name() works
    print(b1.change_customer_name('src/bank_registers/bank.txt', 'Name11', '199911111'))
    '''

    ''' Show that the method add_account() works
    print(b1.add_account('src/bank_registers/bank.txt', '199911111'))
    print(b1.add_account('src/bank_registers/bank.txt', '199911112'))
    print(b1.add_account('src/bank_registers/bank.txt', '199911112'))
    '''

    ''' Show that the method get_account() works
    print(b1.get_account('src/bank_registers/bank.txt', '199911111','ADD_VALID_ACCOUNT_ID'))
    print(b1.get_account('src/bank_registers/bank.txt', '199911111','1a458b49-62f3'))
    '''

    ''' Show that the method deposit() works
    print(b1.deposit('src/bank_registers/bank.txt', '199911111','1a458b49-62f3', 120.0))
    '''

    ''' Show that the method withdraw() works
    print(b1.withdraw('src/bank_registers/bank.txt', '199911111','1a458b49-62f3', 360.0))
    '''

    ''' Show that the method close_account() works
    print(b1.close_account('src/bank_registers/bank.txt', '199911115','1a458b51-62f3'))
    '''


if __name__ == '__main__':
    main()
