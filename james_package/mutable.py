import random

number = random.randint(1, 20)
counter = 0
while counter <= 10:
    trials = int(input("guess the number"))
    if trials == number:
        print("you have won congratulation")
    else:
        print("you have failed, try again")
        counter = counter + 1
if counter > 10:
    print("your trials have ended")








