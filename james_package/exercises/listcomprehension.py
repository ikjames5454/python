listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [m for m in listA if m % 2 == 0]
print(result)

name = [n ** 2 for n in listA]
print(name)

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = ( m for m in listA if m % 2 == 0)
print(result)

name = (n ** 2 for n in listA)
print(name)





