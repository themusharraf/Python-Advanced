def my_decorator(func):
    def wrapper():
        print("Funktsiya ishga tushdi! ")
        func()
        print("Funktsiya tuxtadi! ")
