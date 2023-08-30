j# write a function caled password_validator. the function asks the user to enter a password. A valid password should have at least
# one upper letter, one lower letter, and one number. it should not be less than 8 characters long. When the user enters a password,
# the function should check if the password is valid. if the password is valid, the function should return the valid password.
# if the password is not valid, the function should tell the users the errors in the password and prompt the user to enter another password.

import re
import string


def password_validator():
    while True:

        password = input('Enter a valid password: ')
        special_character = string.punctuation

        if not (len(password) == 8 or len(password) > 8):
            print("The password you entered: " + password + " " + "must be equal or greater than eight")
            continue
        if not re.search(r'[A-Z]', password):
            print("The password you entered: " + password + " " + "must have at least an uppercase letter")
            continue
        if not re.search(r'[a-z]', password):
            print("The password you entered: " + password + " " + "must have at least a lowercase letter")
            continue
        if not re.search(r'[0-9]', password):
            print("The password you entered: " + password + " " + "must have at least a numeric value")
            continue
        if not any(character in special_character for character in password):
            print("The password you entered: " + password + " " + "must have at least a special character")
            continue
        return password


if password_validator():
    print('valid password')

