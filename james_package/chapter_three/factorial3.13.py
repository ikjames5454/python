# factorials) Factorial calculations are common in probability. The factorial of a
# nonnegative inte(Fger n is written n! (pronounced “n factorial”) and is defined as follows:
# 3.13
# n! = n · (n - 1) · (n - 2) · ... · 1
# for values of n greater than or equal to 1, with 0! defined to be 1. So,
# 5! = 5 · 4 · 3 · 2 · 1
# which is 120. Factorials increase in size very rapidly. Write a script that inputs a nonnega-
# tive integer and computes and displays its factorial. Try your script on the integers 10, 20,

number = int(input("enter a non negative number: "))
if number == 0 or number == 1:
    print(f"{number}! is equal to 1")
elif number < 0:
    print("not possible")
else:
    factorial = 1
    while number > 0:
        factorial = factorial * number
        number = number - 1
    print(f" {factorial}")
