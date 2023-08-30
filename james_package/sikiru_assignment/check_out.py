import re
from datetime import datetime

list_item_bought = []
number_of_items = []
price_of_items = []
store = "SEMICOLON STORES"
branch = "MAIN BRANCH"
location = "Location: 312 ALBERT MACAULAY WAY, SABO YABA, LAGOS."
tel = "TEL: 03293828343"
date = datetime.now()
cashier = 0
customer_name = 0
sub_totals = 0
my_discount = 0
amount = 0


def name():

    global customer_name
    names = input("what is the customer,s name:")
    if re.search(r'[a-zA-Z ]+', names):
        customer_name = names
        item_bought()

    else:
        print("must be a valid name:")
        name()



def item_bought():

    global list_item_bought
    item = input("What did the user buy: ")
    list_item_bought.append(item)
    number_of_item()



def number_of_item():
    global number_of_items
    number = input("how many pieces: ")
    if re.search(r'^[0-9]+$', number):
        if int(number) > 0:
            number_of_items.append(int(number))
            price_of_item()
    else:
        print("invalid input, try again: ")
        number_of_item()



def price_of_item():
    global price_of_items
    price = input("How much per unit: ")
    if re.search(r'^[0-9]+$', price):
        if float(price) > 0:
            price_of_items.append(int(price))
            add_more_item()
    else:
        print("invalid input, try again letter: ")
        price_of_item()




def add_more_item():
    option = input("add more item: ")
    num = "yes"
    num1 = "no"
    if option.casefold() == num.casefold():
        item_bought()
    elif option.casefold() == num1.casefold():
        cashier_name()

    else:
        print("invalid input")
        add_more_item()



def cashier_name():
    global cashier
    names = input("What is the cashier's name: ")
    if re.search(r'[a-zA-Z ]+', names):
        cashier = names
        discounts()
    else:
        print("must be a valid name:")
        cashier_name()



def discounts():

    global my_discount
    discount = input("How much discount will he get: ")
    if re.search(r'^[0.0-9.0]+$', discount):
        if float(discount) > 0:
            my_discount = float(discount)
            output()
    else:
        print("invalid input, try again letter: ")
        discounts()


def output():
    print()
    print(store)
    print(branch)
    print(location)
    print(tel)
    print(date)
    print("Cashier: " + str(cashier))
    print("Customers' name: " + f"{customer_name}")
    output2()


def output2():
    global sub_totals
    print("=" * 60)
    print("\t\t" + "ITEM" + "\t\t" + "QTY" + "\t\t\t" + "PRICE" + "\t\t\t" + "TOTAL(NGN)")
    print()
    print("=" * 60)
    sub_total = 0
    for num, number in enumerate(list_item_bought):
        individual_total = number_of_items[num] * price_of_items[num]
        sub_total += individual_total
        sub_totals = sub_total
        print("\t\t" + number + "\t\t" + f'{number_of_items[num]:.2f}' + "\t\t" + f'{price_of_items[num]:.2f}' + "\t\t\t" + f'{individual_total:.2f}')

    output3()


def output3():
    print("_" * 60)
    print("\t\t\t\t\t\t\t" + "Sub Total: " + "\t\t\t" + f'{sub_totals:.2f}')
    discount = sub_totals * (my_discount / 100)
    print("\t\t\t\t\t\t\t" + "Discount: " + "\t\t\t" + f'{discount:.2f}')
    vat = sub_totals * (17.50 / 100)
    bill_total = sub_totals - discount + vat
    print("\t\t\t\t\t\t" + "VAT @ 17.50%: " + "\t\t\t" + f'{discount:.2f}')
    print("=" * 60)
    print("\t\t\t\t\t\t" + "Bill Total: " + "\t\t\t" + f'{bill_total:.2f}')


def request():
    global amount
    print("=" * 60)
    print("THIS IS NOT A RECEIPT KINDLY PAY " + f'{sub_totals:.2f}')
    print("=" * 60)
    print()
    print()
    requests = (input("How much did the user give you: "))
    if re.search(r'^[0.0-9.0]+$', requests):
        if (float(requests)) > 0:
            amount = float(requests)
            output4()
    else:
        print("invalid input, try again : ")
        discounts()


def output4():
    output()
    print("\t\t\t\t\t\t" + "Amount Paid: " + "\t\t\t" + f'{amount:.2f}')
    balance = amount - sub_totals
    print("\t\t\t\t\t\t\t" + "Balance: " + "\t\t\t" + f'{balance:.2f}')
    print("=" * 60)
    print("\t\t" + "THANK YOU FOR YOUR PATRONAGE")
    print("=" * 60)




def main():
    name()
    request()


if __name__ == "__main__":
    main()
