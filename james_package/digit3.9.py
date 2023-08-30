digit_number = int(input("Enter six digit number: "))
for number in range(6,0,-1):
    digit = (digit_number // 10**(number-1)) % 10
    print(digit)
print()


