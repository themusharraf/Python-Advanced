def my_decorator(func):
    print("Funktsiya ishga tushdi! ")
    func()
    print("Funktsiya tuxtadi! ")



def my_func():
    print("hello def my function")


my_decorator(my_func)
# def my_decorator(func):
#     def wrapper():
#         print("Funksiya ishga tushdi!")
#         func()
#         print("Funksiya tuxtadi!")
#
#     return wrapper
#
#
# @my_decorator
# def my_func():
#     print("function ishlab turibdi! ")
#
#
# my_func()
