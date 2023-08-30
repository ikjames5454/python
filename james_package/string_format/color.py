# write a python program to display the first and the last colors from the following list.


color_list = ["Red", "green", "white", "black"]

for color in color_list[0::3]:
    print(color)


def colour():
    color_lists = ["Red", "green", "white", "black"]
    return color_lists[0], color_lists[-1]


print(colour())
