numbers = [10,20,30,40,50]
total = 0
for sums in numbers:
    total = total + sums


print(total)

addition = 0
for sums in numbers[0::2]:
    addition = addition + sums
print(addition)

sums = 0
for summation in numbers[1::2]:
    sums = sums + summation
print(sums)
