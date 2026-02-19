# def toliq_ism_yasa(name, surname):
#     """To'liq ism qaytaruvchi funksiya"""
#     full_name = f"{name} {surname}"
#     print(f"{full_name.title()}")
#
# toliq_ism_yasa('muhammadaziz', 'xabibullayev')
from supabase_auth import model


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
# avtolar = [avto1, avto2]
# print("Onlayn bozorda mavjud bo'lgan mashinalar:")
# for avto in avtolar:
#     if avto['price']:
#         price = avto['price']
#     else:
#         price = "Noma'lum"
#     print(f"{avto['color'].title()} {avto['model'].title()}, Narhi: {price}")

# My own range function as rename oraliq()
# def oraliq(min, max):
#     numbers = []
#     while min < max:
#         numbers.append(min)
#         min += 1
#     return numbers
#
# for num in oraliq(1, 31):
#     print(num)

