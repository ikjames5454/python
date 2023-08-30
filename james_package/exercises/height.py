height = 6
height_needed = int(input("Enter the height: "))
if height_needed == 6 or height_needed > 6:
    print("you are qualified to ride the ferris wheel")
    age_grade = int(input("Enter your age: "))
    if age_grade < 12:
        print("your fee payment is #100")
    elif 12 < age_grade < 60:
        print("your fee payment is #200")
    else:
        print("you have a free pass")
if height_needed < 6:
    print("you are not qualified to take a ride")