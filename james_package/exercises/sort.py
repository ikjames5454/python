numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]
print(numbers[::-1])


def sorted_list(num):
    for a in range(len(num)):
        for b in range(len(num)):
            if num[b] > num[a]:
                num[b], num[a] = num[a], num[b]
    return num


print(sorted_list(numbers))


def even_nunber(num):
    new_num = []
    for numbers in num:
        if numbers % 2 == 0:
            new_num.append(numbers)
    return new_num


result = [a for a in numbers if a % 2 == 0]
print(result)
print(even_nunber(numbers))
