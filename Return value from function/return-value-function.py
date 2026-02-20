# def toliq_ism_yasa(name, surname):
#     """To'liq ism qaytaruvchi funksiya"""
#     full_name = f"{name} {surname}"
#     print(f"{full_name.title()}")
#
# toliq_ism_yasa('muhammadaziz', 'xabibullayev')\
from django.db.models.expressions import result

# def toliq_ism_yasa(name, surname):
#     """To'liq ism qaytaruvchi funksiya"""
#     full_name = f"{name.title()} {surname.title()}"
#     return full_name
#
# student = toliq_ism_yasa('muhammadaziz', 'xabibullayev')
# teacher = toliq_ism_yasa('sanjar', 'shukurov')
# doctor = toliq_ism_yasa('umar', 'adkamov')
#
# print(f"Darsga kelmagan talabalar: {student.title()}")
# print(f"Bugun optolmolog {doctor.title()} ishga kelmadi. U bugun dam oladi.")
# print(f"Programming'dan kiradigan ustozinglar {teacher.title()} bugun betob ekan. Bugun 1 para dars bo'lmaydi.")

# def toliq_ism_yasa(name, surname, middlename=''):
#     if middlename:
#         full_name = f"{name} {surname} {middlename}"
#     else:
#         full_name = f"{name} {surname}"
#     return full_name.title()
#
# student = toliq_ism_yasa('ikrom', 'zokirov', "hoshim ogli")
# print(student)

# def avto_info(company, model, color, box, make_year, price=None):
#     avto = {
#         'company': company,
#         'model': model,
#         'color': color,
#         'box': box,
#         'make_year': make_year,
#         'price': price
#     }
#     return avto
#
# avto1 = avto_info('bmw', 'x7', 'qora', 'avtomat', 2026)
# avto2 = avto_info('gm', 'gentra', 'oq', 'mexanika', 2023, '200,000,000')
# avtolar1 = [avto1, avto2]
# print("Onlayn bozorda mavjud bo'lgan mashinalar:")
# for avto in avtolar1:
#     if avto['price']:
#         price = avto['price']
#     else:
#         price = "Noma'lum"
#     print(f"{avto['color'].title()} {avto['model'].title()}, Narhi: {price}")

# My own range function as rename oraliq()
# def oraliq(min, max, step=None):
#     numbers = []
#     if step is None:
#         step = 1
#
#     while min < max:
#         numbers.append(min)
#         min += step
#     return numbers
#
# for num in oraliq(0, 40, 2):
#     print(num)

# avtolar2 = []
# while True:
#     print("\nSaytimizdagi avtolar ro'yxtatini shakllantiramiz:")
#     company = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     color = input("Ranggi: ")
#     box = input("Karobkasi: ")
#     make_year = input("Ishlab chiqarilgan yili: ")
#     price = float(input("Narhi: "))
#
#     avtolar2.append(avto_info(company, model, color, box, make_year, price))
#
#     result = input("Yana qo'shasizmi? (yes/no): ")
#     if result == 'no':
#         break
#
# print("\nSalonimizdagi avtolar:")
#
# for avto in avtolar2:
#     if avto['price']:
#         price = avto['price']
#     else:
#         price = "No'malum"
#     print(f"{avto['color'].title()} {avto['model'].title()}, {avto['box']} karobka. Narhi: {price}")



# HOMEWORK
# 1. Assignment
# customers = []
# def users(name, surname, age, b_year, b_place, email=None, phone=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     user = {
#         'name': name,
#         'surname': surname,
#         'age': age,
#         'b_year': b_year,
#         'b_place': b_place,
#         'email': email,
#         'phone': phone
#     }
#     return user
#
# while True:
#     name = input("Ismingizni kiriting: ")
#     surname = input("Familiyangizni kiriting: ")
#     age = int(input("Yoshingizni kiriting: "))
#     b_year = int(input("Tug'ilgan yilingizni kiriting: "))
#     b_place = input("Tug'ilgan joyingizni kiriting: ")
#
#     email = input("Email qo'shasizmi? (yes/no): ")
#     if email == 'yes':
#         email = input("Emailingizni kiriting: ")
#     else:
#         print("Rahmat")
#         email = "Noma'lum"
#
#     phone = input("Telefon raqam qo'shasizmi? (yes/no): ")
#     if phone == 'yes':
#         phone = input("Telefon raqamingizni kiriting: ")
#     else:
#         print("Rahmat")
#         phone = "Noma'lum"
#
#     customers.append(users(name, surname, age, b_year, b_place, email, phone))
#     result = input("Yana foydalanuvchi qo'shasizmi? (yes/no): ")
#     if result == 'no':
#         break

# 2. Assignment
# for user in customers:
#     print(f"{user['name'].title()} {user['surname'].title()}, {user['age']} yoshda, ya'ni {user['b_year']} yilda tug'ilgan. "
#           f"{user['name'].title()} {user['b_place'].capitalize()}da tavallud topgan. "
#           f"Uning emaili: {user['email']}, va uning telefon raqami: {user['phone']}")

