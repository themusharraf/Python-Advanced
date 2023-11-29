import timeit


def generators():
    for x in range(10_000):
        yield x


def generator_return():
    temp = []
    for i in generators():
        if i == 1_000:
            break
    return temp


def for_loop():
    temp_list: list[int] = []
    for x in range(10_000):
        temp_list.append(x)

    return temp_list


if __name__ == '__main__':
    time_for = timeit.timeit(stmt=for_loop, number=10_000)
    time_yield = timeit.timeit(stmt=generators, number=10_000)

    print("For loop", round(time_for, 5))
    print("Yield   ", round(time_yield, 5))
    faster = (time_for / time_yield) * 100
    print(f"{(round(faster, 2))} % tez")
