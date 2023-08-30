num = [1, 2, 5, 6, 3, 9, 1, 2, 3, 4, 89, 67, 5, 3]
mem = sorted(num)
print(mem)
targets = 7


def lists(nums, target):
    nums = sorted(nums)
    nun = []
    for i in range(len(nums)):
        if target == nums[i]:
            nun.append(i)
    return nun


print(lists(num, targets))
