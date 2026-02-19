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
# def yosh_hisobla(name, age):
#     """Foydalanuvchi ismini va yoshini so'rab, unga tug'ilgan yilini chiqarib beruvchi funksiya"""
#     print(f"{name.title()} siz {2026-age}-yilda tug'ilgan ekansiz.")
#
# yosh_hisobla(name='akmalxon', age=20)

# 2. Assignment
# def hisobla(number):
#     """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya"""
#     print(f"{number} ning kvadrati {number**2} ga teng\n"
#           f"{number} ning kubi {number**3} ga teng")
#
# hisobla(131)
# hisobla(number=12)

# 3. Assignment
# def juft_toq_chiqar(number):
#     """Foydalanuvchidan son qabul qilib, uni juft yoki toq ekanligini konsolga chiqaradigan funksiya"""
#     if number %2 == 0:
#         print(f"{number} juft son")
#     else:
#         print(f"{number} toq son")
#
# juft_toq_chiqar(71)

# 4. Assignment
# def son_olchash(num1, num2):
#     """Foydalanuvchidan ikkita son qabul qilib,
#     ulardan qaysi biri kattaligini konsolga chiqarish,
#     sonlar teng bo'lsa 'Sonlar teng' deb chiqarish funksiyasi"""
#     if num1 > num2:
#         print(f"{num1} soni {num2} dan katta ekan.")
#     elif num1 == num2:
#         print(f"Sonlar teng!")
#     else:
#         print(f"{num2} soni {num1} dan katta ekan")
#
# son_olchash(8, 4)
# son_olchash(19, 132)

# 5. Assignment
# def solishtir(x, y):
#     """Foydalanuvchidan x va y sonlarni olib, uni konsolga chiqaruvchi funksiya"""
#     if x > y:
#         print(f"{x} - {y} dan katta ekan.")
#     elif x == y:
#         print(f"{x} - {y} teng ekan.")
#     else:
#         print(f"{y} - {x} dan katta ekan.")
#
# solishtir(221, 241)

# 6. Assignment
# def solishtir(x, y=2):
#     """Foydalanuvchidan x va y sonlarni olib, uni konsolga chiqaruvchi funksiya. y ga 2 sonni default holatda berib ko'rdim."""
#     if x > y:
#         print(f"{x} - {y} dan katta ekan.")
#     elif x == y:
#         print(f"{x} - {y} teng ekan.")
#     else:
#         print(f"{y} - {x} dan katta ekan.")
#
# solishtir(221)
# solishtir(y=13, x=3)

# 7. Assignment
# def tekshir(number):
#     """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarni qoldiqsiz bo'linishini tekshiruvchi funksiya"""
#     for n in range(1, 11):
#         if not number % n:
#             print(f"{number} soni {n} ga qoldiqsiz bo'linadi")
#
# tekshir(41035707)