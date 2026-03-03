# import avto
from avto import Avto, Bus, Train

car1 = Avto('GM', 'Malibu', 'black', 30000, 1000)
car2 = Avto('BMW', 'X8', 'white', 353000, 19000)
car3 = Avto('Toyota', 'KSI 21', 'blue', 11000, 12000)

print(car3.model)
print(Avto.get_num_avto())
