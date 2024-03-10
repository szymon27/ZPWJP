def a(names):
    for name in names:
        print(name)


def bv1(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] * 2
    return arr


def bv2(arr):
    return [i * 2 for i in arr]


def c(arr):
    for item in arr:
        if item % 2 == 0:
            print(item)


def d(arr):
    for i in range(len(arr)):
        if i % 2 == 0:
            print(arr[i])


if __name__ == '__main__':
    a(['jan', 'szymon', 'wiktor', 'natalia', 'krzysiek'])
    print(bv1([2, 3, 4, 5, 6]))
    print(bv2([2, 3, 4, 5, 8]))
    c(range(0, 9))
    d(range(0, 100))
