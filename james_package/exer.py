# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("true,the number is even")
# else:
#     print("false,not even")
#
def check_even():
   number = int(input("Enter a number: "))
   if number % 2 == 0:
    print("true,the number is even")
   else:
    print("f    ")
print()
check_even()

for a in range(10,0,-1):
    for b in range(a):
        print("#",end=" ")
    print()
print()

for a in range(10,0,-1):
    for b in range(10-a):
        print(" ",end=" ")
    for b in range(a):
        print("#",end=" ")
    print()
print()

for a in range(1,11):
    for b in range(10-a):
        print(" ",end=" ")
    for b in range(a):
        print("#",end=" ")
    print()

# check_even()


# def check_even(number):
#     if number % 2 == 0:
#         print("true,the number is even")
#     else:
#         print("false,not even")
#
#
# check_even(5)
# check_even(16)
# check_even(5)
# check_even(10)


def check_even(number):
    return number % 2 == 0


print(check_even(16))
print(check_even(5))
print(check_even(10))
