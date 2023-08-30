for r in range (1,10):
    for f in range(r):
        print("*",end=" ")
    for b in range(9-r):
        print( " ",end=" ")
    for b in range(9-r):
        print(" ",end=" ")
    for f in range(r-1):
        print("*",end=" ")
    for f in range(r):
        print("*",end=" ")
    for b in range(9 - r):
        print(" ", end=" ")
    for b in range(9 - r):
        print(" ", end=" ")
    for f in range(r):
        print("*", end=" ")
    for f in range(r-1):
        print("*",end=" ")
    print()
for r in range(9,0,-1):
    for f in range(r):
        print("*",end=" ")
    for b in range(9-r):
        print(" ",end=" ")
    for b in range(9-r):
        print(" ",end=" ")
    for f in range(r):
        print("*",end=" ")
    for f in range(r-1):
        print("*",end=" ")
    for b in range(9 - r):
        print(" ", end=" ")
    for b in range(9 - r):
        print(" ", end=" ")
    for f in range(r):
        print("*", end=" ")
    for f in range(r-1):
        print("*", end=" ")
    print()