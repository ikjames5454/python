print("see him big head")

first_name = input("Enter firstname")
if first_name == " " or first_name is None:
    exit()
last_name = input("Enter lastname")
age = int(input("age"))
print("Your name is" + first_name + last_name)
print("your age", age)
if age < 0:
    print("Age can not be negative")
elif age < 18:
    print("you are underage")
elif age > 65:
    print("you are an old man")
else:
    print("you are a youth")







