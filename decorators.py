def my_decorator(func):
    print("Funktsiya ishga tushdi! ")
    func()
    print("Funktsiya tuxtadi! ")


def my_func():
    print("hello def my function")


my_decorator(my_func)
