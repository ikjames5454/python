class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self):
        print(f"drawing from point {self.a} to {self.b}")

    def __str__(self):
        return f"({self.a}, {self.b})"


p1 = Example(1, 2)
p2 = Example(5, 6)

print(p1)
print(p2)

