# print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tMultiplication Table\n")
#
for number in range(1, 13):
    for num in range(1, 13):
        result = number * num
        # print('%i X %i = %-5i' % (num, number, result), end="\t\t\t")
        print(f"{number} x {num} = {number * num}",end="\t\t\t\t\t\t\t")
    print()


# def check_multiplication_function_1():
#     check_multiplication_function_1 = int(input("Enter the multiplication number: "))
#     for number in range(1, 2):
#         for one in range(1, 13):
#             if check_multiplication_function_1 == 1:
#                 print(f"{number} x {one} = {number * one}")
#     for number in range(2, 3):
#         for one in range(1, 13):
#             if check_multiplication_function_1 == 2:
#                 print(f"{number} x {one} = {number * one}")
#     for number in range(3, 4):
#         for one in range(1, 13):
#             if check_multiplication_function_1 == 3:
#                 print(f"{number} x {one} = {number * one}")
#     for number in range(4, 5):
#         for one in range(1, 13):
#             if check_multiplication_function_1 == 4:
#                 print(f"{number} x {one} = {number * one}")
#     for number in range(5, 6):
#         for one in range(1, 13):
#             if check_multiplication_function_1 == 5:
#                 print(f"{number} x {one} = {number * one}")
#     for number in range(6, 7):
#         for one in range(1, 13):
#             if check_multiplication_function_1 == 6:
#                 print(f"{number} x {one} = {number * one}")
#     for number in range(7, 8):
#         for one in range(1, 13):
#             if check_multiplication_function_1 == 7:
#                 print(f"{number} x {one} = {number * one}")
#     for number in range(8, 9):
#         for one in range(1, 13):
#             if check_multiplication_function_1 == 8:
#                 print(f"{number} x {one} = {number * one}")
#     for number in range(9, 10):
#         for one in range(1, 13):
#             if check_multiplication_function_1 == 9:
#                 print(f"{number} x {one} = {number * one}")
#     for number in range(10, 11):
#         for one in range(1, 13):
#             if check_multiplication_function_1 == 10:
#                 print(f"{number} x {one} = {number * one}")
#     for number in range(11, 12):
#         for one in range(1, 13):
#             if check_multiplication_function_1 == 11:
#                 print(f"{number} x {one} = {number * one}")
#     for number in range(12, 13):
#         for one in range(1, 13):
#             if check_multiplication_function_1 == 12:
#                 print(f"{number} x {one} = {number * one}")
#
#
# check_multiplication_function_1()
#
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tMultiplication Table\n")


def check_multiplication_table():
    x = int(input("Enter the number: "))
    for number in range(1,13):
        for num in range(1,x):
            result = number * num

            # if multiplication_table == 20:
            print('%i X %i = %-5i' % (num, number, result), end="\t\t\t")

        print()


check_multiplication_table()

# for x in range(1,3):
#     for y in range(1,9):
#         print(f"Outer loop {x},inner loop {y}")
#
