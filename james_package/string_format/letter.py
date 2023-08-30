import re


def check():
    enter = input("enter vowel letter: ")
    if re.search(r'[a e i o u]', enter):
        print("is vowel letter")
    else:
        print("not a vowel letter")


check()
