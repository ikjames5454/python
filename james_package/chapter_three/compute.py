compute_positive_number = 0
compute_negative_number = 0
sums = 0
number = 0
average = 0


while True:
    compute = int(input("Enter either positive number or negative (or 0 to break): "))
    if compute == 0:
        break

    sums = sums + compute
    number = number + 1

    if compute > 0:
        compute_positive_number = compute_positive_number + 1

    if compute < 0:
        compute_negative_number = compute_negative_number + 1
    average = sums / number
if number == 0:
    print("no number other than zero")


print("The positive number is: ", compute_positive_number)
print()
print("The negative number is: ", compute_negative_number)
print()
print("the total is: ", f"{sums:.2f}")
print()
print("The average is: ", f"{average:.2f}")



