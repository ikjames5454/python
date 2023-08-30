def number():
    while True:
        try:

            enter = int(input("enter a number between 1500 and 2700: "))
            if 1500 <= enter <= 2000:
                if enter % 7 == 0 and enter:
                    print("is divisible by 7 and a multiple of 5")
                else:
                    print("is not divisible by 7 and is not a multiple of 5")
                    break
            else:
                print(" is not within the range")
        except (ValueError, KeyboardInterrupt):
            print("not a floating value:")


number()
