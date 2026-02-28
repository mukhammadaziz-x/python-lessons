# WORK WITH OBJECTS
# class Student:
#     def __init__(self, name, surname, b_year):
#         self.name = name
#         self.surname = surname
#         self.b_year = b_year
#         self.level = 1
#
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.name
#
#     def get_surname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.surname
#
#     def get_byear(self):
#         """Talabaning tug'ilgan yilini qaytaradi"""
#         return self.b_year
#
#     def set_newlevel(self, new_level):
#         """Talabaning bosqichini yangilash funksiyasi"""
#         self.level = new_level
#
#     def update_level(self):
#         """Talabaning bosqichini 1 taga ko'paytirib beradi"""
#         self.level += 1
#
#     def get_info(self):
#         """Talabaning to'liq ma'lumotini qaytaradi"""
#         return f"{self.name} {self.surname}, {self.level}-bosqich talabasi."
#
#     def get_fullname(self):
#         """Talabaning to'liq ismini qaytaradi"""
#         return f"{self.name} {self.surname}"
#
#     def get_age(self, year):
#         """Talabaning yoshini aniqlovchi funksiya"""
#         return year - self.b_year
#
# user1 = Student('Muhammadaziz', 'Xabibullayev', 2006)
from List.list import cars


# user1.set_newlevel(2)
# print(user1.get_info())
# print(user1.get_age(2030))
# print(user1.get_byear())
# print(user1.set_newlevel(3))
# print(user1.get_info())

# class Subject:
#     def __init__(self, name):
#         self.name = name
#         self.student_count = 0
#         self.students = []
#
#     def add_student(self, student):
#         self.students.append(student)
#         self.student_count += 1
#
#     def get_student(self):
#         return [x.get_fullname() for x in self.students] # Easiest method
#
#         # talabalar = []
#         # for x in self.students:
#         #     talabalar.append(x.get_fullname())
#         # return talabalar # Hardest method
#
#     def get_students_num(self):
#         return self.student_count
#
# def see_methods(klass):
#     return [method for method in dir(klass) if not method.startswith('__')]
#
# math = Subject('Math')
# student1 = Student('Muhammadaziz', 'Xabibullayev', 2006)
# student2 = Student('Yaxyo', 'Anvarov', 2008)
# student3 = Student('Akbarshoh', 'Qurbonov', 2006)
# math.add_student(student1)
# math.add_student(student2)
# math.add_student(student3)

# print(math.get_student())

# print(math.students)
# print(math.student_count)

# print(math.students[0].get_info())

# print(student1.__dict__)
# print(student1.__dict__.keys())
# print(see_methods(student1))

# HOMEWORK
# 1. Assignment
class Avto:
    def __init__(self, model, color, box, price, km=0):
        self.model = model
        self.color = color
        self.box = box
        self.price = price
        self.km = km

    cars = []

    def get_info(self):
        return f"{self.color.capitalize()} {self.model}, {self.box} karobka. Narhi: {self.price}"

    def update_km(self, num):
        if num > 0:
            self.km += num
        else:
            print("Kilometrni kamaytirib bo'lmaydi.")

class Avtosalon:
    def __init__(self, salon_name, address):
        self.salon_name = salon_name
        self.address = address
        self.cars_in_sale = []

    def add_car(self, car):
        self.cars_in_sale.append(car)

    def get_cars_info(self):
        return [car.get_info() for car in self.cars_in_sale]

# Mashina yaratamiz:
car1 = Avto('BMW', 'black', 'auto', '$150,000')
car2 = Avto('Mercedes benz', 'white', 'auto', '$350,000')

# Avtosalon yaratamiz:
my_salon = Avtosalon('General Motors', 'Tashkent, Mirzoulugbek')

# Mashinani salonga qo'shamiz:
my_salon.add_car(car1)
my_salon.add_car(car2)

# Kilometrni yangilaymiz:
car1.update_km(5000)

print(f"Salondagi mashinalar: ({my_salon.salon_name})")
for info in my_salon.get_cars_info():
    print(f"- {info}")

print("Methodlarni tekshirish:")
print(f"Birinchi avto hususiyatlari: {car1.__dict__}")


str_methods = [method for method in dir(str) if not method.startswith('__')]
print(f"str klass metodlari (bir qism): {str_methods[:10]}")