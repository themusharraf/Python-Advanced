def generators():
    for x in range(10_000):
        yield x


def for_loop():
    temp_list: list[int] = []
    for x in range(10_000):
        temp_list.append(x)

    return temp_list


if __name__ == '__main__':
    ...
