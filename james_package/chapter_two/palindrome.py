def is_palindrome(string):
    enter = input("enter a name: ")
    if string == string[:: -1]:
        return True
    else:
        return False


is_palindrome("peep")
