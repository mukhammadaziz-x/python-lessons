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
