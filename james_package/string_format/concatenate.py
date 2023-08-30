lists = ["name", "mike", "john"]


def concatenates(element):
    concatenation = "".join(map(str, element))
    return concatenation


result = concatenates(lists)
print(result)
