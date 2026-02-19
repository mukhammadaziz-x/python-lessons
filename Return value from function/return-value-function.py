# def toliq_ism_yasa(name, surname):
#     """To'liq ism qaytaruvchi funksiya"""
#     full_name = f"{name} {surname}"
#     print(f"{full_name.title()}")
#
# toliq_ism_yasa('muhammadaziz', 'xabibullayev')

def toliq_ism_yasa(name, surname):
    """To'liq ism qaytaruvchi funksiya"""
    full_name = f"{name.title()} {surname.title()}"
    return full_name

student = toliq_ism_yasa('muhammadaziz', 'xabibullayev')
teacher = toliq_ism_yasa('sanjar', 'shukurov')
doctor = toliq_ism_yasa('umar', 'adkamov')

print(f"Darsga kelmagan talabalar: {student.title()}")
print(f"Bugun optolmolog {doctor.title()} ishga kelmadi. U bugun dam oladi.")
print(f"Programming'dan kiradigan ustozinglar {teacher.title()} bugun betob ekan. Bugun 1 para dars bo'lmaydi.")


