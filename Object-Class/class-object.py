# x = 10
# print(type(x))
# matn = 'salom'
# print(type(matn))
# print(matn.upper())
# print(x.upper())

# def salom():
#     print("Assalamu alaykum")
#
# salom()

# CLASS
class Student:
    def __init__(self, name, surname, b_year):
        self.name = name
        self.surname = surname
        self.b_year = b_year

    def tanishtir(self):
        print(f"Ismim {self.name} familiyam {self.surname}, tug'ilgan yilim {self.b_year}")

student1 = Student('Muslima', 'Faxriddinova', 2000)
student2 = Student('Xojiakbar', 'Toshtemirov', 2006)
student3 = Student('Yaxyo', 'Anvarov', 2008)

# print(student1.surname)
# print(student3.b_year)
# print(student2.name))
student2.tanishtir()