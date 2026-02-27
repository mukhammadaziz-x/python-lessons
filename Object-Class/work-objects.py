# WORK WITH OBJECTS
class Student:
    def __init__(self, name, surname, b_year):
        self.name = name
        self.surname = surname
        self.b_year = b_year
        self.level = 1

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.name

    def get_surname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.surname

    def get_byear(self):
        """Talabaning tug'ilgan yilini qaytaradi"""
        return self.b_year

    def set_newlevel(self, new_level):
        """Talabaning bosqichini yangilash funksiyasi"""
        self.level = new_level

    def update_level(self):
        """Talabaning bosqichini 1 taga ko'paytirib beradi"""
        self.level += 1

    def get_info(self):
        """Talabaning to'liq ma'lumotini qaytaradi"""
        return f"{self.name} {self.surname}, {self.level}-bosqich talabasi."

    def get_fullname(self):
        """Talabaning to'liq ismini qaytaradi"""
        return f"{self.name} {self.surname}"

    def get_age(self, year):
        """Talabaning yoshini aniqlovchi funksiya"""
        return year - self.b_year

user1 = Student('Muhammadaziz', 'Xabibullayev', 2006)

# user1.set_newlevel(2)
# print(user1.get_info())
# print(user1.get_age(2030))
# print(user1.get_byear())
# print(user1.set_newlevel(3))
# print(user1.get_info())