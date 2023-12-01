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
# def my_decorator(func):
#     def wrapper():
#         print("Funksiya start")
#         func()
#         print("Funksiya stop!")
#
#     return wrapper
#
#
# @my_decorator
# def my_func():
#     s = []
#     print("function ishlab turibdi! ")
#     for x in range(200000_000):
#         s.append(x)
#
#
# my_func()

# ________________________________________________________________
# def divide_decorator(func):
#     def divide_inner(a, b):
#         try:
#             return func(a, b)
#         except ZeroDivisionError:
#             print("Nolga bo'lish mumkin emas!")
#
#     return divide_inner
#
#
# def second_zero(func):  # zero 0 - > 1 function
#     def inner(a, b):
#         if b == 0:
#             b += 1
#         return func(a, b)
#
#     return inner
#
#
# @second_zero
# @divide_decorator
# def divider(a, b):
#     return a / b
#
#
# print(divider(10, 5))  # 2.0
# print(divider(10, 0))  # 10.0

data_list = []


def register_api(func):
    data_list.append(func)
    return func


@register_api
def get_api():
    return "name-> Admin"


def get_api1():
    return "name-> User"


def get_api2():
    return "name-> username"


if __name__ == "__main__":
    for i in data_list:
        print(i())
