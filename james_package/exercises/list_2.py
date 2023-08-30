# numbers = [10, 20, 30, 40, 50]
# for number in range(len(numbers)):
#     numbers[number] = numbers[number] ** 2
#
# print(numbers)
# new_number = numbers[0:]

numbers = [30, 50, 10, 40, 20]

largest_number = numbers[0] ** 2
smallest_number = numbers[0] ** 2

for number in range(len(numbers)):
    numbers[number] = numbers[number] ** 2
    if numbers[number] > largest_number:
        largest_number = numbers[number]
    if numbers[number] < smallest_number:
        smallest_number = numbers[number]
    difference = largest_number - smallest_number
print(numbers)
print(difference)
print(smallest_number)
print(largest_number)
