# def my_decorator(func):
#     print("Funktsiya ishga tushdi! ")
#     func()
#     print("Funktsiya tuxtadi! ")
#
#
# def my_func():
#     print("hello def my function")
#
#
# my_decorator(my_func)
# ________________________________________________________________
def my_decorator(func):
    def wrapper():
        print("Funksiya start")
        func()
        print("Funksiya stop!")

    return wrapper


@my_decorator
def my_func():
    s = []
    print("function ishlab turibdi! ")
    for x in range(200000_000):
        s.append(x)


my_func()
