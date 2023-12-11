from functools import lru_cache


# @lru_cache(maxsize=10000)
# def fib(n):
#     if n in {0, 1}:  # Base case n == 1 or n == 2 return 1
#         return n
#     return fib(n - 1) + fib(n - 2)  # Recursive case
#
#
# print(fib(500))
