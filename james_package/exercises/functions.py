set1 = {1, 3, 4, 4, 5, 5, 5, 6, (1, 2, 3, 4), (1, 2, 3, 4)}
print(set1)
set2 = ([2])
print(type(set2))


def highest_odd_numbers(nums):
    highest_odd_number = None

    for num in nums:
        if num % 2 != 0 and (highest_odd_number is None or num > highest_odd_number):
            highest_odd_number = num
    return highest_odd_number


number = [1, 2, 4, 7, 89, 9, 33, 5, 9, 10]
print(highest_odd_numbers(number))


print(max([counter for counter in number if counter % 2 != 0]))


set1 = {4,5 }
set2 = {4,5,6,7,8,9}
print(set1.union(set2))

