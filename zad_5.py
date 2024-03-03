def fun(a: list, b: int) -> bool:
    found = False
    for item in a:
        if item == b:
            found = True
    return found

if __name__ == '__main__':
    print(fun([1,2,3,4,5], 5))