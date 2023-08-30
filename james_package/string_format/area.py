import math


def areas(radius):
    while True:
        try:
            if  radius > 0:
                print(math.pi * (radius ** 2))
                break
            else:
                print("must be greater than zero")
                break
        except (ValueError, KeyboardInterrupt):
            print("not  right")
    # radius = float(input("enter the radius of a circle: "))
    # pie = 3.142
    # area = pie * radius ** 2
    # print("r = ", radius)
    # print("Area = " + f'{area:.2f}')
    # if radius < 0:
    #     raise ValueError
    # if type(radius) is not int and type(radius) is not float:
    #     raise TypeError
    # return math.pi * (radius ** 2)



areas(4)





