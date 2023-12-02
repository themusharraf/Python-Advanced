def fib(n: int):
    a: int = 0
    b: int = 1
    print(a)
    print(b)
    for x in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)
fib(6)