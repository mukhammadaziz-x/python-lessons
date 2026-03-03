# Encapsulation
from uuid import uuid4

from reportlab.graphics.charts.piecharts import theta0


class Avto:
    __num_avto = 0
    # PI = 3.14159
    def __init__(self, make, model, color, price, km):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1

    # def get_km(self):
    #     return self.__km
    #
    # def get_id(self):
    #     return self.__id
    #
    # def add_km(self, km):
    #     if km >= 0:
    #         self.__km += km
    #     else:
    #         print("Mashina km kamaytirib bo'lmaydi")

    @classmethod # Decorator
    def get_num_avto(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi.")

car1 = Avto('GM', 'Malibu', 'black', 30000, 1000)
car2 = Avto('BMW', 'X8', 'white', 353000, 19000)
car3 = Avto('Toyota', 'KSI 21', 'blue', 11000, 12000)

print(Avto.get_num_avto())

# car1.add_km(150)
# print(car1.get_km())