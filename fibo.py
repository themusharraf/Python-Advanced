# def fib(n: int):
#     a: int = 0
#     b: int = 1
#     print(a)
#     print(b)
#     for x in range(2, n):
#         c = a + b
#         a = b
#         b = c
#         print(c)
# fib(1000)

from functools import lru_cache



def fib(n):
    if n in {0, 1}:  # Base case n == 1 or n == 2 return 1
        return n
    return fib(n - 1) + fib(n - 2)  # Recursive case


print(fib(100))
# for x in range(15):
#     print(fib(x))
