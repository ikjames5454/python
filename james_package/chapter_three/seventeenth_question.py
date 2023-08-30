# for a in range(1):
#     print("*")
#     for b in range(2):
#         print("*",end=" ")
#     print()
#     for c in range(3):
#         print("*",end=" ")
#     print()

for a in range(1,11):
    for b in range(a):
        print("*",end = " ")
    print()
print()

for a in range(10,0,-1):
    for b in range(a):
        print("*",end=" ")
    print()
print()

for a in range(10,0,-1):
    for b in range(10-a):
        print(" ",end=" ")
    for b in range(a):
        print("*",end=" ")
    print()
print()

for a in range(1,11):
    for b in range(10-a):
        print(" ",end=" ")
    for b in range(a):
        print("*",end=" ")
    print()





