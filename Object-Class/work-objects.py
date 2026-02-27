# WORK WITH OBJECTS
class Student:
    def __init__(self, name, surname, b_year):
        self.name = name
        self.surname = surname
        self.b_year = b_year
        self.level = 1

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_byear(self):
        return self.b_year

    def set_newlevel(self, new_level):
        self.level = new_level

    def update_level(self):
        self.level += 1

    def get_info(self):
        return f"{self.name} {self.surname}, {self.level}-bosqich talabasi."

    def get_fullname(self):
        return f"{self.name} {self.surname}"

    def get_age(self, year):
        return year - self.b_year

user1 = Student('Muhammadaziz', 'Xabibullayev', 2006)
user1.set_newlevel(2)
print(user1.get_info())
