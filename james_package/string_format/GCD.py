import math


# def divisor(num1, num2):
#     return math.gcd(num1, num2)
#
#
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# result = divisor(number1, number2)
# print(result)
#
#
# def multiple(num1, num2):
#     return math.lcm(num1, num2)
#
#
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# result = multiple(number1, number2)
# print(result)


def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def compute_lcm(a, b):
    gcd = compute_gcd(a, b)
    lcm = (a * b) // gcd
    return lcm

# Input two positive integers
num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))

lcm_result = compute_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {lcm_result}")