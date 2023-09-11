lists = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']


def splitting(loop, num):
    return [loop[nums::num] for nums in range(num)]


p = splitting(lists, 3)

print(p)


def split(nums):
    n = []
    i = 5
    for num in range(i):
        n.append(nums[num::4])
    return n


print(split(lists))

# p = splitting(lists, 3)
#
# print(p)
#
#
# def iterate(num: int):
#     list_in = []
#     for x in range(num):
#         list_in.append(x * 2)
#     return list_in
#
#
# print(iterate(100))
#
#
# def generator_func(num):
#     for x in range(num):
#         yield x
#
#
# g = generator_func(100)
# for c in g:
#     pass
#
# a = generator_func(1000)
# next(a)
# next(a)
# next(a)
#
# print(next(a))
