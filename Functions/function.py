# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalamu alaykum!")
#
# salom_ber()

# def salom_ber(name):
#     """Foydalanuvchidan ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f"Assalamu alaykum, hurmatli {name.title()}!")
#
# salom_ber('muhammadaziz')
# salom_ber('muhammadyusuf')
#
# print(salom_ber.__doc__)
# print(print.__doc__)
# print(max.__doc__)

# def fullname(firstname, surname):
#     """Foydalanuvchini ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {firstname.title()}")
#     print(f"Foydalanuvchi familiyasi: {surname.title()}")
#
# fullname('muhammadaziz', 'xabibullayev')

# def yosh_hisobla(name, b_day):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{name.title()} {2026-b_day} yoshda.")

# yosh_hisobla('muhammadaziz', 2006)
# yosh_hisobla(name='Abdulloh', b_day=2006)

# def yosh_hisobla(b_day, cur_y=2026):
#     """Foydalanuvchi tug'ilagan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {cur_y-b_day} yoshdasiz.")
#
# yosh_hisobla(2006)

# HOMEWORK
# 1. Assignment
def yosh_hisobla(name, age):
    """Foydalanuvchi ismini va yoshini so'rab, unga tug'ilgan yilini chiqarib beruvchi funksiya"""
    print(f"{name.title()} siz {2026-age}-yilda tug'ilgan ekansiz.")

yosh_hisobla(name='akmalxon', age=20)

# 2. Assignment
def hisobla(number):
    """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya"""
    print(f"{number} ning kvadrati {number**2} ga teng\n"
          f"{number} ning kubi {number**3} ga teng")

hisobla(131)
hisobla(number=12)