import re


def your_vat():
    while True:
        try:
            price = float(input("Enter the price of an item: "))
            vat = float(input("Enter the VAT: "))




            if not price > 0:
                print(" your price of item can not be less than zero or be negative number")
                continue
            elif not vat > 0:
                print("your vat can not be less than 0 or negative number")
                continue
            else:
                price_vat = (price * vat) / 100
                vat_price = price + price_vat
                print(price_vat)

                return vat_price

        except (ValueError, KeyboardInterrupt):
            print("not a floating value:")





print(your_vat())
