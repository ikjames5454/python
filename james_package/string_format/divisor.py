def integers():
    num1= int(input("Enter the two numbers: "))
    num2 = int(input("enter the numbers: "))
    if num1 % 2 == 0 and num2 % 2 == 0:
        return 2
    elif num1 % 3 == 0 and num2 % 3 == 0:
        return 3
    elif num1 % 4 == 0 and num2 % 4 == 0:
        return 4


print(integers())
