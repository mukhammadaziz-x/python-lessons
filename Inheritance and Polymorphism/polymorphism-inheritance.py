class Shaxs:
    def __init__(self, name, surname, passport, id, birth_date, address):
        self.name = name
        self.surname = surname
        self.__passport = passport
        self.__id = id
        self.__birth_date = birth_date
        self.__address = address
        self.people_count = []

    def get_passport(self):
        return self.__passport

    def get_id(self):
        return self.__id

    def get_birthdate(self):
        return self.__birth_date

    def get_address(self):
        return self.__address

    def get_info(self):
        info = f"{self.name} {self.surname}. "
        info += f"Passport: {self.__passport}, {self.__birth_date}-yilda tug'ilgan."
        return info

class Subject:
    def __init__(self, name):
        self.name = name


class Student(Shaxs):
    def __init__(self, name, surname, passport, id, birth_date, address, rating, scholarship, list_subjects, student_id):
        super().__init__(name, surname, passport, id, birth_date, address)
        self.__rating = rating
        self.__scholarship = scholarship
        self.__list_subjects = list_subjects
        self.__student_id = student_id
        self.level = 1
        self.students_count = []

    def fanga_yozil(self, fan_obyekti):
        if fan_obyekti in (fan_obyekti, Subject):
            self.subjects.append(fan_obyekti)
            print(f"{fan_obyekti.name} fani qo'shildi!")
        else:
            print("Bu fan emas!")

    def get_info(self):
        info = f"{self.name} {self.surname}. "
        info += f"Passport: {self.passport}, {self.b_year}-yilda tug'ilgan. "
        info += f"Student ID: {self.student_id}. "
        info += f"{self.name} O'zbekiston {self.address.region} shahrida tug'ilgan. U hozirda {self.address.district} tumani, {self.address.street} ko'chasida {self.address.home}-uyda yashab kelmoqda."
        return info

    def remove_fan(self, fan_nomi):
        topildi = False
        for fan in self.subjects:
            if fan.name == fan_nomi:
                self.subjects.remove(fan)
                topildi = True
                print(f"{fan_nomi} o'chirildi.")
                break

        if not topildi:
            print("Siz bu fanga yozilmagansiz.")

    def get_subjects(self):
        return [fan.name for fan in self.subjects]

class Address:
    def __init__(self, home, street, district, region):
        self.home = home
        self.street = street
        self.district = district
        self.region = region

    def get_address(self):
        address = f"{self.region} viloyati, {self.district} tumani, "
        address += f"{self.street} ko'chasi, {self.home}-uy."
        return address

# HOMEWORK
# 1. Assignment
class Professor(Shaxs):
    def __init__(self, name, surname, passport, b_year, degree, university):
        super().__init__(name, surname, passport, b_year)
        self.degree = degree
        self.university = university

    def get_info(self):
        info = f"{self.name} {self.surname}. "
        info += f"Ilmiy darajasi: {self.degree}. {self.university}da ishlaydi."
        return info

# Fanlar yaratamiz
math = Subject('Oliy matematika')
dasturlash = Subject('Python dasturlash')

# Manzilni talabaga qo'shamiz
address1 = Address(49, 'Objuvoz', "Xamdo'stlik", 'Andijan')

# Talaba yaratamiz
student1 = Student('Muhammadaziz', 'Xabibullayev', 'AD1883210', 2006, '0000012', address1)
print(student1.get_info())

# Fanga yozilamiz
student1.fanga_yozil(math)
student1.fanga_yozil(dasturlash)

# Fanlarni ko'ramiz va o'chiramiz
print(f"Fanlar ro'yxati: {student1.get_subjects()}")
student1.remove_fan('Oliy matematika')
student1.remove_fan('Tarix')

# Professor yaratamiz
professor1 = Professor('Andrew', 'Huberman', 'DA23111', 1975, 'PHD', 'Stanford')
print(professor1.get_info())