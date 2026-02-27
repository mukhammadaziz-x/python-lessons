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

# # CLASS
# class Student:
#     def __init__(self, name, surname, b_year):
#         self.name = name
#         self.surname = surname
#         self.b_year = b_year
#
#     def get_name(self):
#         return self.name
#
#     def get_lastname(self):
#         return self.surname
#
#     def get_age(self, year):
#         return year - self.b_year
#
#     def tanishtir(self):
#         return f"Ismim {self.name} familiyam {self.surname}, tug'ilgan yilim {self.b_year}"
#
# student1 = Student('Muslima', 'Faxriddinova', 2000)
# student2 = Student('Xojiakbar', 'Toshtemirov', 2006)
# student3 = Student('Yaxyo', 'Anvarov', 2008)

# print(student1.surname)
# print(student3.b_year)
# print(student2.name))

# print(student2.tanishtir())
# print(student2.get_name())
# print(student2.get_lastname())
# print(student2.get_age(2026))

# HOMEWORK
# 1. Assignment
class User:
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

user1 = User('muhammadaziz', 'mukhammadaziz-x', 'muhammadazizxabibullayev@gmail.com', 'vdf3%d#fd*$0')
user2 = User('abdulloh', 'abdulloh', 'abdulloh@gmail.com', 'vdf3%d#fdf2$0')
user3 = User('muhammadyusuf', 'mukhammadaziz-x', 'muhammad-yusuf@gmail.com', 'v3gdf3%fd*$0')
