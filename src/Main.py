from classes.Account import Account
from classes.Bank import Bank
from classes.Customer import Customer


def main():    
    b1 = Bank('Nordea')
    # The file location is set to be run with the script file
    b1._load('src/bank_registers/bank.txt')

    #a1 = Account()
    #c1 = Customer()


if __name__ == '__main__':
    main()
