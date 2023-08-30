book = {
    "title": "wonders made",
    "author": "michael",
    "isbn": 1212112222,
    "price": 500
     }
for key, value in book.items():
    print(key,value)
for key in book.keys():
    print(key)
for value in book.values():
    print(value)
book.update({"colour": "black"})
book.update({"title": "james"})
book2 = book.copy()
print(book)
print(book2)
print(book.clear())
print(book)