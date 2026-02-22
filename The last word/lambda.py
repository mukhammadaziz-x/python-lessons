# import math
from math import sqrt

# uzunlik = lambda pi, r: 2 * pi * r
# print(uzunlik(math.pi, 10))
#
# kvadrat = lambda x, y: x ** y
# print(kvadrat(5, 3))

# def daraja(n):
#     return lambda x: x ** n
#
# kvadrat = daraja(2) # bu kvadrat chiqarish kodi, daraja(2) bu yerdagi 2 funksiyani n ga berilgan qiymati. Kvadrat o'zgaruvchi nomini lambda uchun berdik, chunki lambda nomsiz funksiya hisoblanadi. Hozir foydalanuvchi argument kiritsa lambda uchun kiritadi. Masalan: n -> daraja(2), x -> lambda x, foydalanuvchi kiritadigan argument.
# kub = daraja(3) # bu yerda ham tepada yozganimdek ishlaydi, faqat funksiya uchun 3 argument berilgan.
# print(f"3-ning kvadrati {kvadrat(3)} ga, "
#       f"kubi {kub(3)} ga teng")

# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)

# # Map metodi yordamida, hamda o'zimiz yaratib olgan daraja2() funksiyasi bilan ro'yxat ichidagi sonlar kvadratini qaytardik.
# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x * x
# print(daraja2(5))

# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
#
# print(list(map(daraja2, sonlar)))

# # Lambda yordamida ro'yxat ichidagi sonlar kvadratini qaytardik.
# sonlar = list(range(11))
# kvadratlar = list(map(lambda x: x*x, sonlar))
# print(kvadratlar)

# Agar labmda funksiyasini ishlatmasdan kod yozganimizda bunday ko'rinishda bo'lar edi.
sonlar = list(range(11))
kvadratlar = []
for son in sonlar:
    kvadratlar.append(son * son)
print(kvadratlar)