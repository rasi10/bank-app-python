from classes.Account import Account
from classes.Bank import Bank
from classes.Customer import Customer


def main():
    a1 = Account(12)
    b1 = Bank(12)
    c1 = Customer(10)
    a1.print_account()
    b1.print_bank()
    c1.print_customer()
    a1.test(c1)


if __name__ == '__main__':
    main()
