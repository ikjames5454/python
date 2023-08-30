def is_palindrome(string):


     return string[:: -1]


print(is_palindrome("hello"))



def reverse(name):
    for context in name:
        context = name[:: -1]
    return context


print(reverse("hello"))



string = "Hello girl"
s = string.split()[::-1]
l = []
for i in s:
    l.append(i)

print(" ".join(l))
