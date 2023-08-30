duplicate = [1, 2, 2, 2, 24, 5, 5, 8, 9, 9, 9]


def remover(duplication):
    new_list = []
    for element in duplication:
        if element not in new_list:
            new_list.append(element)
    return new_list

print(remover(duplicate))

def remove(duplication):
    new = []
    for element in duplication:
        if element not in new:
            new += [element]
    return new


print(remove(duplicate))

harry = [1, 2, 2, 2, 24, 5, 5, 8, 9, 9, 9]
harry = set(harry)
harry = list(harry)
print(harry)

def list(word):
    dup = [i for i in word if word.count(i) == 1]

    return dup

lists = [1, 2, 2, 2, 24, 5, 5, 8, 9, 9, 9]

print(list(lists))


list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4]


def functions(collector):
    length = 0
    for element in collector:
        length += 1
    return length


print(functions(list))







