# (Palindromes) A palindrome is a number, word or text phrase that reads the same
# backwards or forwards. For example, each of the following five-digit integers is a palin-
# drome: 12321, 55555, 45554 and 11611. Write a script that reads in a five-digit integer
# and determines whether it’s a palindrome. [Hint: Use the // and % operators to separate
# the number into its digits.]

number = int(input("Enter five digit: "))
number_1 = number // 10000
number_2 = (number % 10000) // 1000
number_3 = (number % 1000) // 100
number_4 = (number % 100) // 10

number_5 = number % 10
print(number_1,number_2,number_3,number_4,number_5)
palindrome = (number_1 == number_5) and (number_2 == number_4)

if palindrome:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")



