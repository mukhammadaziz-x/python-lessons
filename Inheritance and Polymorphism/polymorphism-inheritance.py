class Shaxs:
    def __init__(self, name, surname, passport, b_year):
        self.name = name
        self.surname = surname
        self.passport = passport
        self.b_year = b_year

    def get_info(self):
        info = f"{self.name} {self.surname}. "
        info += f"Passport: {self.passport}, {self.b_year}-yilda tug'ilgan."
        return info

class Subject:
    def __init__(self, name):
        self.name = name


class Student(Shaxs):
    def __init__(self, name, surname, passport, b_year, student_id, address):
        super().__init__(name, surname, passport, b_year)
        self.student_id = student_id
        self.address = address
        self.level = 1
        self.subjects = []

    def fanga_yozil(self, fan_obyekti):
        if fan_obyekti not in (fan_obyekti, Subject):
            self.subjects.append(fan_obyekti)
            print(f"{fan_obyekti.name} fani qo'shildi")
        else:
            print("Bu fan emas!")

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
        info += f"{self.b_year}-yilda tug'ilgan. {self.name}ning {self.diploma} diplomi bor."
        return info

    def get_diploma(self):
        return self.diploma

    def set_diploma(self, new_diploma):
        self.diploma = new_diploma

class School(Address):
    def __init__(self, school_name, school_year, school_rating, name, surname, passport, b_year, diploma, school):
        self.school_name = school_name
        self.school_year = school_year
        self.school_rating = school_rating

school1 = School('Harvard', 4, 3, )
professor1 = Professor('Andrew', 'Huberman', 'DA23111', 1975, 'PHD Standford school of Medicine')


student1_address = Address(49, 'Objuvoz', 'Andijan', 'Andijan')
student1 = Student('Muhammadaziz', 'Xabibullayev', 'AD1883210', 2006, '0000012', student1_address)
print(student1.address.get_address())