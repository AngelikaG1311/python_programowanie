class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (
            f" Property:\n"
            f" Area:{self.area} m2\n"
            f" Rooms:{self.rooms}\n"
            f" Price:{self.price} PLN\n"
            f" Address:{self.address}\n"
        )


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f" House:\n"
            f" Area:{self.area} m2\n"
            f" Rooms:{self.rooms}\n"
            f" Price:{self.price} PLN\n"
            f" Address:{self.address}\n"
            f" Plot size:{self.plot} m2\n"
        )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f" Flat:\n"
            f" Area:{self.area} m2\n"
            f" Rooms:{self.rooms}\n"
            f" Price:{self.price} PLN\n"
            f" Address:{self.address}\n"
            f" Floor size:{self.floor}\n")


house = House(150, 5, 1000000, "Krakow, ul. Dworcowa 1", 9)
flat = Flat(30, 2, 500000, "Krakow, ul. Wielicka 7", 5)
print(house)
print(flat)
