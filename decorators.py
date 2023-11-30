def my_decorator(func):
    def wrapper():
        print("Funktsiya ishga tushdi! ")
        func()
        print("Funktsiya tuxtadi! ")

    return wrapper


@my_decorator
def add_function(a: int, b: int, ) -> int:
    return a + b


print(add_function(3, 5))
