# 3.2
# (What’s Wrong with This Code?) What is wrong with the following code?
# a = b = 7
# print('a =', a, '\nb =', b)
a = b = 7
print("a =",a,"\nb =",b)

# 3.3
# (What Does This Code Do?) What does the following program print?
# for row in range(10):
# for column in range(10):
# print('<' if row % 2 == 1 else '>', end='')
# print()


for row in range(10):
    for column in range(10):
        print("<" if row % 2 == 1 else "",end="")
print()


# 3.4
# (Fill in the Missing Code) In the code below
# for ***:
# for ***:
# print('@')
# print()
# replace the *** so that when you execute the code, it displays two rows, each containing
# seven @ symbols, as in:
# @@@@@@@
# @@@@@@@


for a in range(3):
    for b in range(7):
        print("@",end="")
    print()