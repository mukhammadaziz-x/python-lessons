from uuid import uuid4

class Shaxs:
    __num_people = 0
    def __init__(self, name, surname, age, passport, birth_date, address): # 'id' olib tashlandi, chunki u pastda uuid4() bilan yaratilyapti
        self.name = name
        self.surname = surname
        self.age = age
        self.__passport = passport
        self.__id = uuid4()
        self.__birth_date = birth_date
        self.__address = address
        Shaxs.__num_people += 1

    @classmethod
    def get_peopleNum(cls):
        return cls.__num_people

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
    __students_count = 0
    # Argumentlar Shaxs klassiga moslandi
    def __init__(self, name, surname, age, passport, birth_date, address, rating, scholarship, list_subjects, student_id):
        super().__init__(name, surname, age, passport, birth_date, address)
        self.__rating = rating
        self.__scholarship = scholarship
        self.__list_subjects = list_subjects if isinstance(list_subjects, list) else [] # Ro'yxat bo'lishini ta'minlash
        self.__student_id = student_id
        self.level = 1
        Student.__students_count += 1

    @classmethod
    def get_studentCount(cls):
        return cls.__students_count

    def fanga_yozil(self, fan_obyekti):
        # Tekshirish mantiqi to'g'irlandi
        if isinstance(fan_obyekti, Subject):
            self.__list_subjects.append(fan_obyekti)
            print(f"{fan_obyekti.name} fani qo'shildi!")
        else:
            print("Bu fan emas!")

    def get_info(self):
        # Student.get_passport() emas, self.get_passport() bo'lishi kerak
        info = f"{self.name} {self.surname}. "
        info += f"Passport: {self.get_passport()}, {self.get_birthdate()}-yilda tug'ilgan. "
        info += f"Student ID: {self.__student_id}. "
        # Address obyektidan get_address() metodini chaqirish
        manzil_matni = self.get_address().get_address()
        info += f"{self.name} hozirda O'zbekiston, {manzil_matni}da yashab kelmoqda."
        return info

    def remove_fan(self, fan_nomi):
        topildi = False
        for fan in self.__list_subjects:
            if fan.name == fan_nomi:
                self.__list_subjects.remove(fan)
                topildi = True
                print(f"{fan_nomi} o'chirildi.")
                break
        if not topildi:
            print("Siz bu fanga yozilmagansiz.")

    def get_subjects(self):
        return [fan.name for fan in self.__list_subjects]

class Professor(Shaxs):
    def __init__(self, name, surname, age, passport, birth_date, address, degree, university):
        super().__init__(name, surname, age, passport, birth_date, address)
        self.degree = degree
        self.university = university

    def get_info(self):
        return f"{self.name} {self.surname}. Ilmiy darajasi: {self.degree}. {self.university}da ishlaydi."

class Address:
    def __init__(self, home, street, district, region):
        self.home = home
        self.street = street
        self.district = district
        self.region = region

    def get_address(self):
        return f"{self.region} viloyati, {self.district} tumani, {self.street} ko'chasi, {self.home}-uy."

# HOMEWORK
# 1. Manzil yaratish
address1 = Address(49, 'Objuvoz', "Xamdo'stlik", 'Andijan')

# 2. Fanlar yaratish
math = Subject('Oliy matematika')
dasturlash = Subject('Python dasturlash')

# 3. Talaba yaratish (Argumentlar soni va tartibi to'g'irlandi)
student1 = Student('Muhammadaziz', 'Xabibullayev', 20, 'AD1883210', 2006, address1, 1, 34000, [], 'AD132411')
print(student1.get_info())

# Fanga yozilish
student1.fanga_yozil(math)
student1.fanga_yozil(dasturlash)

# Fanlarni ko'rish va o'chirish
print(f"Fanlar ro'yxati: {student1.get_subjects()}")
student1.remove_fan('Oliy matematika')

# 4. Professor yaratish (Argumentlar to'g'irlandi)
professor1 = Professor('Andrew', 'Huberman', 48, 'DA23111', 1975, address1, 'PHD', 'Stanford')
print(professor1.get_info())