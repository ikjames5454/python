def string():
    user = input("enter a name: ")
    numbers = int(input("enter the number: "))
    if len(user) < 2:
        return f'{user} ' * numbers
    else:
        return  f'{user[:2]} ' * numbers



print(string())
