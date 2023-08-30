sum_of_number = 0
multiplication_of_number = 1
smallest_number = None
largest_number = None
for integer in range(1, 5):
    number = int(input("Enter the integer number: "))

    sum_of_number = sum_of_number + number
    multiplication_of_number = multiplication_of_number * number
    if smallest_number is None or number < smallest_number:
        smallest_number = number
    if largest_number is None or number > largest_number:
        largest_number = number
average = sum_of_number / 4
print("sum_of_number: ",sum_of_number)
print("multiplication_of_number: ",multiplication_of_number)
print("average",average)
print("smallest_number",smallest_number)
print("largest_number",largest_number)
