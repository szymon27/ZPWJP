def fun(a: list, b: list) -> list:
    ret = list(set(a + b))
    for i in range(len(ret)):
        ret[i] = ret[i] ** 3
    return ret


if __name__ == '__main__':
    print(fun([1, 2, 3, 4], [4, 4, 4]))
