number = 5
counter = 0
while counter <= 10:
    trials = int(input("guess a right number between 1 to 10: "))
    if trials < number:
        print("too low, try again: ")

    elif trials > number:
        print("too high, try again: ")

    elif trials == number:
        print("you have won")
        break
    else:
        counter = counter + 1

if counter > 10:
    print("you have exceeded number of triers")




