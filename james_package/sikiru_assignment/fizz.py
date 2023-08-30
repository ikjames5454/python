def function_number():
    for number in range(1, 101):
        if number % 5 == 0 and number % 3 == 0:
            print("fizz buzz")
            continue
        elif number % 3 == 0:
            print("fizz")
            continue
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


print(function_number())
