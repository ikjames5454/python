weight1 = int(input("Enter the weight1 for the package: "))
price1 = float(input("Enter the price1 for the package: "))
weight2 = int(input("Enter the weight2 in the package: "))
price2 = float(input("Enter the price2 in the package: "))
price_one = weight1 / price1
price_two = weight2 / price2

if price_one > price_two:
    print("Package 2 has a better price.")
else:
    print("Package 2 has a better price.")
