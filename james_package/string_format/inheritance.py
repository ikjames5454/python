from james_package.string_format.Exception import DogException


class Animal:
    def __init__(self):
        self.number_of_nose = 1

    def eat(self):
        print("eating")


class Dog(Animal):
    def __init__(self):
        self.number_of_leg = 4
        super().__init__()

    @property
    def number_of_leg(self):
        return self.number_of_leg

    @number_of_leg.setter
    def number_of_legs(self, value):
        if value != 4:
            raise DogException ("invalid number of legs")
        self.number_of_leg = value

    def waik(self):
        print(f"walking with {self.number_of_leg}")


class Fish(Animal):
    def swim(self):
        print("swimming")


fi = Fish()
fi.number_of_nose
