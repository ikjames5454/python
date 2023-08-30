def is_palindrome():
    name = input("enter a name: ")
    if name.casefold() == name[:: -1].casefold():
        return True
    else:
        return False


print(is_palindrome())
