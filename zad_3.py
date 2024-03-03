def is_even(x: int) -> bool:
    return x % 2 == 0

if __name__ == '__main__':
    even = is_even(55)
    if even:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")