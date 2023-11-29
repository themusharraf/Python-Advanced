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
    gen = generators()
