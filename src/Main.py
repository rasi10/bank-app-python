from classes.Account import Account
from classes.Bank import Bank
from classes.Customer import Customer


def main():
    b1 = Bank('Nordea')
    # The file location is set to be run with the script file
    # customers = b1._load('src/bank_registers/bank.txt')    

    # customers = b1.get_customers('src/bank_registers/bank.txt')
    # print(customers)

    customer = b1.get_customer('src/bank_registers/bank.txt', '199911111')
    print(customer)


if __name__ == '__main__':
    main()
