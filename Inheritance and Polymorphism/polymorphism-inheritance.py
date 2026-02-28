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

    def get_age(self, year):
        return year - self.b_year

class Student(Shaxs):
    def __init__(self, name, surname, passport, b_day, id):
        super().__init__(name, surname, passport, b_day)
        self.id = id
        self.level = 1

    def get_id(self):
        return self.id

    def get_level(self):
        return self.level

    def get_info(self):
        info = f"{self.name} {self.surname}. "
        info += f"{self.get_level()}-bosqish, ID: {self.get_id()}"
        return info

student = Student('Muhammadaziz', 'Xabibullayev', 'AD1882429', 2006, 'N0000011')

print(student.get_age(2026))
print(student.get_info())