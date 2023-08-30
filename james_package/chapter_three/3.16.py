# (Nested Control Statements) Use a loop to find the two largest values of 10 num-
# bers entered.
# 3.16
third_largest_number = 0
largest_number = 0
second_largest_number = 0
number = 1
while number <= 10:
    numbers = int(input("Enter the number: "))
    number = number + 1

    if numbers > largest_number:
        third_largest_number = second_largest_number
        second_largest_number = largest_number
        largest_number = numbers
    elif numbers > second_largest_number:
        third_largest_number = second_largest_number
        second_largest_number = numbers
    elif numbers > third_largest_number:
        third_largest_number = numbers

    elif numbers < 0:
        print("don,t accept negative number")
        break
print("the largest number is: ",largest_number)
print("the second largest number:",second_largest_number)
print(third_largest_number)


