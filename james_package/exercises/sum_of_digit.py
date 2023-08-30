digit = int(input("Enter the digit number: "))
digit_1 = digit // 100
digit_2 = (digit % 100) // 10
digit_3 = digit % 10
sums = digit_1 + digit_2 + digit_3
print(digit_1 , digit_2, digit_3)
print(sums)
