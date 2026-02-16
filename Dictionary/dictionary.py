# car_0 = {'model':'ferrari', 'color':'red'}
# print(car_0['model'])
# print(car_0['color'])

# student_0 = {'fullname':'muhammadaziz xabibullayev', 'age':20, 'b_day':2006}
# print(f"{student_0['fullname'].title()},\
#       {student_0['age']},\
#       {student_0['b_day']}")

# student_0['faculty'] = 'information subject'
# student_0['course'] = 2
# print(student_0)

# student_1 = {}
# student_1['first_name'] = 'Muhammadaziz'
# student_1['last_name'] = 'Xabibullayev'
# student_1['age'] = 20
# student_1['course'] = 2
# student_1['major'] = 'Python'
#
# print(f"Student {student_1['first_name']} {student_1['last_name']}, {student_1['course']}-nd year.")
#
# del student_1['age']
# print(student_1)

# phones = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
# }
# # print(phones)
# print(phones.get('alli', 'there isn\'t name'))

# HOMEWORK
# 1. Assignment
# dad = {
#     'name':'xamidulloh',
#     'b_day':1981,
#     'city':'andijan',
#     'address':'objuvoz street, 49-home'
# }
# mom = {
#     'name':'hilola',
#     'b_day':1983,
#     'city':'andijan',
#     'address':'farovon street, 13-home'
# }
# bro_1 = {
#     'name':'muhammadyusuf',
#     'b_day':2008,
#     'city':'andijan',
#     'address':'objuvoz street, 49-home'
# }
# bro_2 = {
#     'name':'abdulloh',
#     'b_day':2022,
#     'city':'andijan',
#     'address':'uzbekistan street, 5-home'
# }
# granny = {
#     'name':'barchinoy',
#     'b_day':1961,
#     'city':'andijan',
#     'address':'to\'xtasin keldi street, 42-home'
# }
#
# print(f"My granny's name is {granny['name'].title()}, she was born in {granny['b_day']}, in the {granny['city'].title()} city.")
# print(f"My father's name is {dad['name'].title()}, he was born in {dad['b_day']}, in the {dad['city'].title()} city.")
# print(f"My mother's name is {mom['name'].title()}, she was born in {mom['b_day']}, in the {mom['city'].title()} city.")
# print(f"My brother's name is {bro_1['name'].title()}, he was born in {bro_1['b_day']}, in the {bro_1['city'].title()} city.")
# print(f"My little brother's name is {bro_2['name'].title()}, he was born in {bro_2['b_day']}, in the {bro_2['city'].title()} city.\n")

# 2. Assignment
# favorite_meals = {
#     'granny': 'palov',
#     'dad': 'kebab',
#     'mom': 'stew',
#     'bro_1': 'pizza',
#     'bro_2': 'jarkop'
# }
# print(f"Barchinoy's favorite food is {favorite_meals['granny'].title()}")
# print(f"Xamidulloh's favorite food is {favorite_meals['dad'].title()}")
# print(f"Hilola's favorite food is {favorite_meals['mom'].title()}")
# print(f"Muhammadyusuf's favorite food is {favorite_meals['bro_1'].title()}")
# print(f"Abdulloh's favorite food is {favorite_meals['bro_2'].title()}")

# 3. Assignment
# python_dict = {
#     'str': 'string - matn',
#     'int': 'integer - butun son',
#     'float': 'float pointing numbers - o\'nlik kasr son',
#     'boolean': 'boolean - True/False - rost va yolg\'on',
#     'list': 'list - ro\'yxat',
#     'tuple': 'tuple - o\'zgarmas ro\'yxat',
#     'dict': 'dictionary - lug\'at',
#     'if': 'if - agar shart bajaruvchisi',
#     'else': 'else - aks holda shart bajaruvchisi',
#     'elif': 'elif - aks holda agar shart bajaruvchi',
#     'for': 'for - uchun tsikli'
# }
# print(python_dict)

# 4. Assignment
# word = input("Enter the word you want: ").lower()
# en_uz = {
#     'apple': 'olma',
#     'cherry': 'olcha',
#     'phone': 'telefon',
#     'laptop': 'noutbuk',
#     'dairy': 'kundalik',
#     'snake': 'ilon'
# }
# print(en_uz.get(word, 'Such a word doesnt exist.'))

# 5. Assignment
# translate = en_uz.get(word)
# if translate == None:
#     print("Such a word doesn't exist.")
# else:
#     print(translate.title())

# PRACTICE
# 1. Assignment
# car = {
#     'model': 'Chevrolet',
#     'color': 'oq',
#     'make_year': 2024
# }
# print(f"Meningn mashinam {car['make_year']}-yilda ishlab chiqarilgan, rangi {car['color']}.")

# car['box'] = 'avtomat'
# car['price'] = 30000
# del car['color']

# print(car)

# 2. Assignment
# countries = {
#     'Uzbekistan': 'Tashkent',
#     'Tajikistan': 'Dushanbe',
#     'Afghanistan': 'Kabul',
#     'Kyrgyzstan': 'Bishkek',
#     'Kazakhstan': 'Astana',
#     'Turkmenistan': 'Ashgabat'
# }
# country = input("O'zingiz hohlagan davlat nomini yozing: ")
# capital = countries.get(country, "Kechirasiz, bizda bu davlat haqida ma'lumot yo'q")
# print(f"{country}ning poytaxti {capital}")

# 3. Assignment
# books = {
#     'ilm olish sirlari': 173,
#     "o'tkan kunlar": 575,
#     'savdogarlar ustozi 1': 240,
#     'pythonda dasturlash asoslari': 290,
#     'savdogarlar ustozi 2': 220
# }

# query = input("O'zingiz o'qigan kitob nomini yozing: ").lower()
# if query in books:
#     print(f"{query.capitalize()} juda zo'r asar, u {books[query]} betdan iborat.")
# else:
#     doesnt_exist = int(input(f"Bizda bunday kitob haqida ma'lumotimiz yo'q ekan. Iltimos ushbu {query.title()} kitob necha sahifaligini yozib yuboring: "))
#     books[query] = doesnt_exist
#     print("Rahmat, yangi kitobni ro'yxatga qo'shib qo'ydim.")
#
# print(books)
