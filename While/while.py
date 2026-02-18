# name = input("What is your name?: ")
# print(f"Hi, {name.title()}")

# name = input("What is your name?: ")
# question = f"Hi {name.title()}. How old are you?: "
# age = input(question)

# name = input("What is your name?: ")
# question = f"Hi {name.title()}. How old are you?: "
# age = input(question)
# age = int(age)
# height = input("How many meters tall are you?: ")
# height = float(height)

# WHILE
# num = 1
# while num <= 5:
#     print(num)
#     num += 1

# print("Kiritilgan sonning kvadratini chiqaruvchi dastur.")
# question = "Istalgan son kiriting "
# question += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# value = ''
# while value != 'exit':
#     value = input(question)
#     if value != 'exit':
#         print(float(value)**2)

# SIGN
# print("Kiritilgan sonning kvadratini chiqaruvchi dastur.")
# question = "Istalgan son kiriting "
# question += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# sign = True
# while sign:
#     value = input(question)
#     if value == 'exit':
#         sign = False
#     else:
#         print(float(value)**2)

# BREAK
# print("Kiritilgan sonning kvadratini chiqaruvchi dastur.")
# question = "Istalgan son kiriting "
# question += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
# while True:
#     value = input(question)
#     if value == 'exit':
#         break
#     else:
#         print(float(value)**2)

# numbers = list(range(1, 11))
# for num in numbers:
#     if num == 5:
#         break
#     else:
#         print(f"{num} ning kvadrati {num**2} ga teng.")

# CONTINUE
# numbers = list(range(1, 11))
# for num in numbers:
#     if num == 5:
#         continue
#     else:
#         print(f"{num} ning kvadrati {num**2} ga teng.")

# num = 0
# while num < 10:
#     num += 1
#     if num % 2 != 0:
#         continue
#     else:
#         print(num)


# Continue
# num = 0
# while num < 10:
#     num += 1
#     if num % 2 != 0:
#         continue
#     else:
#         print(num)

# infinite loop
# num = 0
# while num < 10:
#     # num += 1 # biz buni yozishni unutdik.
#     if num % 2 != 0:
#         continue
#     else:
#         print(num)

# num = 0
# while num < 10:
#     # bu yerda yozilishi kerak
#     if num % 2 != 0:
#         continue
#     else:
#         print(num)
#     num += 1 # biz bu yerda bu qismni noto'g'ri yozdik, tepada yozilishi kerak edi.

# num = 1
# while num > 0:
#     num += 1
#     if num % 2 != 0:
#         continue
#     else:
#         print(num)

# HOMEWORK
# 1. Assignment
# question = "Yaxshi ko'rgan kitoblaringizni kiriting "
# question += "(va 'stop' so'zini yozib dasturni yakunlang): "
# book = ''
# while book != 'stop':
#     book = input(question)
#     if book == 'stop':
#         print("Dastur to'xtadi.")

# 2. Assignment
# question = "Muzeyga kirish uchun yoshingizni ayting "
# question += "('quit' yoki 'exit' so'zini yozib dasturni yakunlang): "
#
# sign = True
# while sign:
#     ticket = input(question).lower()
#
#     if ticket == 'quit' or ticket == 'exit':
#         print("Xaridingiz uchun rahmat!")
#         sign = False
#     else:
#         age = int(ticket)
#         if age <= 7:
#             price = 2000
#         elif age <= 18:
#             price = 3000
#         elif age < 65:
#             price = 10000
#         else:
#             price = 0
#
#         if price == 0:
#             print(f"Siz uchun kirish bepul!")
#         else:
#             print(f"Siz uchun kirish narhi {price} so'm")

# 3. Assignment
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#
#     son = float(qiymat)
#
#     if son < 0:
#         continue
#     else:
#         ildiz = son**(0.5)
#         print(f"{son} ning ildizi {son} ga teng")