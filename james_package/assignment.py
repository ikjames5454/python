for a in range(1, 11):
    for b in range(a):
        print("#", end=" ")
    for b in range(11 - a):
        print("", end=" ")
    for b in range(11 - a):
        print("", end=" ")
    for b in range(11 - a):
        print("#", end=" ")
    for b in range(a):
        print("", end=" ")
    for b in range(a):
        print("", end=" ")
    for b in range(a):
        print("", end=" ")
    for b in range(a):
        print("", end=" ")
    for b in range(11 - a):
        print("#", end=" ")
    for b in range(11 - a):
        print("", end=" ")
    for b in range(11 - a):
        print("", end=" ")
    for b in range(a):
        print("#", end=" ")

    print()
print()


# print()
#
# for a in range(10,0,-1):
#     for b in range(a):
#         print("#",end=" ")
#     print()
# print()
#
# for a in range(10,0,-1):
#     for b in range(10-a):
#         print(" ",end=" ")
#     for b in range(a):
#         print("#",end=" ")
#     print()
# print()
#
# for a in range(1,11):
#     for b in range(10-a):
#         print(" ",end=" ")
#     for b in range(a):
#         print("#",end=" ")
#     print()

def check_number(c):
    for a in range(c):
        for b in range(a + 1):
            print("#", end=" ")
        for b in range(a,c):
            print("", end=" ")
        for b in range(a,c):
            print("", end=" ")
        for b in range(a,c):
            print("#", end=" ")
        for b in range(a + 1):
            print("", end=" ")
        for b in range(a + 1):
            print("", end=" ")
        for b in range(a + 1):
            print("", end=" ")
        for b in range(a + 1):
            print("", end=" ")
        for b in range(a,c):
            print("#", end=" ")
        for b in range(a,c):
            print("", end=" ")
        for b in range(a,c):
            print("", end=" ")
        for b in range(a + 1):
            print("#", end=" ")
        print()


check_number(15)
# check_number(15)
