from models.House import House
from models.Flat import Flat


if __name__ == '__main__':
    house = House(111, 5, 1000000, "Adr1", 500)
    flat = Flat(45, 3, 300000, "Adr2", 2)
    print(house)
    print(flat)
