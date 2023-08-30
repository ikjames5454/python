# def sum1(n):
#     total = 0
#     for counter in range(1, n + 1):
#         total = total + counter
#     print(total)
#
#
# sum1(10)
# sum1(20)
# print()


# def main():
#     sum1(10)
#     sum1(20)
#     sum1(30)
#
#
# def sum1(n):
#     total = 0
#     for counter in range(1, n + 1):
#         total = total + counter
#     print(total)
#
#
# print()

# num = int(input("enter a number"))
#
#
# def sum2():
#     total = 0
#     for counter1 in range(1, num):
#         total = total + counter1
#     print(total)


# sum2()


def greater(num1, num2, num3, num4):
    maximum = num1
    if num2 > maximum:
        maximum = num2
    if num3 > maximum:
        maximum = num3
    if num4 > maximum:
        maximum = num4
    print("maximum is: ", maximum)

    minimum = num1
    if num2 < minimum:
        minimum = num2
    if num3 < minimum:
        minimum = num3
    if num4 < minimum:
        minimum = num4
    print("minimum is: ",minimum)


greater(299,443,23,9)
