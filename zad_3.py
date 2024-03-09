class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Area: {self.area} Rooms: {self.rooms} Price: {self.price}$ Address: {self.address}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"{super().__str__()} Plot: {self.plot}"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"{super().__str__()} Floor: {self.floor}"


if __name__ == '__main__':
    house = House(111, 5, 1000000, "Adr1", 500)
    flat = Flat(45, 3, 300000, "Adr2", 2)
    print(house)
    print(flat)