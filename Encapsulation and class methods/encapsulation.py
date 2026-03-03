# Encapsulation
from uuid import uuid4
class Avto:
    def __init__(self, make, model, color, price, km):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        self.__km = km
        self.__id = uuid4()

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")

car1 = Avto('GM', 'Malibu', 'black', 30000, 1000)

car1.add_km(150)
print(car1.get_km())