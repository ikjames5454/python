while True:
     password = input("enter the password")
     my_password = len(password)
     if my_password < 8:
        print("not the password, enter another password")
     if my_password >= 8:
       print("your password is secure and the length is:",my_password)
       break




for X in range(10):
       print("X")
       for character in "ACECLAN":
           print(character)
