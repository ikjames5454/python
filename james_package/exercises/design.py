from time import time


def sign(n):
    print("*" * 20)
    n()
    print("*" * 20)
    return n


def signs(n):
    def wrap(*args, **kwargs):
        time1 = time()
        result = n(*args, **kwargs)
        time2 = time()
        print(f"IT took {time2 - time1} to execute")
        return result

    return wrap


@sign
@signs
def welcome():
    print("welcome back")
