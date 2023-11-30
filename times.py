import time


def fun():
    result: list[int] = []
    for i in range(100000):
        result.append(i)


start = time.time()
fun()
end = time.time()

natija = end - start
print("Dastur sekund oladi: ", natija)
