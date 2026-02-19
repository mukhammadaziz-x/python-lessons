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

def yosh_hisobla(name, b_day):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{name.title()} {2026-b_day} yoshda.")

yosh_hisobla('muhammadaziz', 2006)
