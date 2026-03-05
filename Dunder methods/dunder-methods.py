from List.list import prices


class Avto:
    __num_avto = 0
    def __init__(self, make, model, color, year, price):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        Avto.__num_avto += 1

    def __repr__(self):
        return f"Avto: {self.make} {self.model}"

    def __eq__(self, y):
        return self.price == y.price

    def __lt__(self, y):
        return self.price < y.price

    def __le__(self, y):
        return self.price <= y.price

class Avtosalon:
    def __init__(self, name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"


avto1 = Avto('GM', 'Malibu', 'black', 2020, 30000)
avto2 = Avto('GM', 'Lacetti', 'white', 2020, 20000)
print(avto1)