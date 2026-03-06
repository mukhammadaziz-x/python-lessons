# student_0 = {
#     'name': 'muhammadaziz',
#     'surname': 'xabibullayev',
#     'age': 20,
#     'faculty': 'programmer',
#     'course': 2
# }
#
# # print(student_0.items())
#
# for key, value in student_0.items():
#     print(f"Key: {key}")
#     print(f"Value: {value}")
#
# phones = {
#     'ali': 'iphone x',
#     'vali': 'samsung s9',
#     'olim': 'mi 10 pro',
#     'abdukarim': 'iphone 8+',
#     'orif': 'nokia 3310',
#     'madina': 'huawei p90 lite',
#     'abdumannop': 'iphone x',
#     'zulayho': 'techo spark 30',
#     'muslima': 'iphone 8+'
# }
#
# for key, value in phones.items():
#     print(f"{key.title()}'s phone is a {value.title()}")
#
# fruits = {
#     'apple': 10000,
#     'pineapple': 13000,
#     'grape': 8200,
#     'orange': 15000,
#     'apricot': 11500,
# }
# print("Products in the store:")
# for product in fruits.keys():
#     print(product.title())
#
# market_list = ['pomegranate', 'grape', 'apple', 'blackberry', 'strawberry']
# for product in fruits:
#     if product in market_list:
#         print(f"{product.title()} {fruits[product]}")
#
# for item in market_list:
#     if item not in fruits:
#         print(f"Please, bring the {item} to your store.")
#
# print("Users use the following phone:")
# for phone in phones.values():
#     print(phone.title())
#
# print("Users use the following phone:")
# for phone in set(phones.values()):
#     print(phone.title())
#
# # HOMEWORK
# # 1. Assignment
# python_dict = {
#     'str': 'matn',
#     'int': 'butun son',
#     'float': 'o\'nlik son/kasr son',
#     'bool': 'rost/yolg\'on',
#     'list': 'ro\'yxat',
#     'dict': 'lug\'at',
#     'set': 'tartiblanmagan va takrorlanmaydigan lug\'at',
#     'tuple': 'o\'zgarmas lug\'at'
# }
# for key, value in sorted(python_dict.items()):
#     print(f"{key.title()} - {value.capitalize()}")
#
# # 2. Assingment
# countries = {
#     'algeria': 'algiers',
#     'angola': 'luanda',
#     'egypt': 'cairo',
#     'ethiopia': 'addis ababa',
#     'ghana': 'accra',
#     'kenya': 'nairobi',
#     'nigeria': 'abuja',
#     'south africa': 'pretoria',
#     'zimbabwe': 'harare'
# }
#
# for country, capital in sorted(countries.items()):
#     print(f"Country: {country.title()}")
#     print(f"Capital: {capital.title()}")
#
# # 3. Assignment
# country = input("Which country's capital would you like to know?: ").lower()
# capital = countries.get(country)
# if capital == None:
#     print("Sorry, we don't have any information about this.")
# else:
#     print(f"The capital of {country.title()} is {capital.title()}")
#
# # 4. Assingment
# menu = {
#     'palov': 40000,
#     'kebab': 20000,
#     'narin': 25000,
#     'manty': 5000,
#     'hanum': 7000,
#     'samsa': 10000,
#     'tukhum barak': 15000,
#     'mashhurda': 50000,
#     'dolma': 43000,
#     'lagman': 35000
# }
# for i in range(3):
#     order = input(f"Choose your {i+1}-meal: ").lower()
#
# if order in menu:
#     print(f"The price of the {order.title()} you chose is {menu[order]} so'm.")
# else:
#     print("We don't have such food.")
#
# # PRACTICE
# # 1. Assignment
# query = input("Dasturlash tilini yozing va uning reytingini bilib oling: ").lower()
# rating = {
#     'python': 95,
#     'java': 80,
#     'c++': 75,
#     'javaScript': 88,
#     'go': 70
# }
#
# for lang in sorted(rating):
#     print(lang)
#
# for score in sorted(rating.values(), reverse=True):
#     print(score)
#
# if query in rating:
#     print(f"{query.title()} dasturlash tili {rating[query]} reytingda turar ekan.")
# else:
#     print("Bu til haqida bizda ma'lumot yo'q.")
#
# # 2. Assignment
# interests = {
#     'muhammadumar': 'kitob o\'qish',
#     'siddiq': 'suhbatlashish',
#     'muhammadali': 'dizayn chizish',
#     'asadulloh': 'cs 1.6 o\'ynash',
#     'fayzulloh': 'futbol o\'ynash',
#     'akbarshoh': 'anime ko\'rish',
#     'yahyoxon': 'do\'stlar bilan birga yurish',
#     'otabke aka': 'kod yozish',
#     'munisa': 'tadbirlarda faol qatnashish',
#     'shohnazar aka': 'futbol o\'ynash',
#     'faxriddin': 'cs 1.6 o\'ynash'
# }
#
# for names in interests:
#     print(names.capitalize())
#
# print("Do'stlarimiz orasida quyidagi qiziqishlar bor: ")
# for hobby in set(interests.values()):
#     print(f"{hobby.capitalize()}")
#
# # 3. Assignment
# fruits = {
#     'apple': 5000,
#     'banana': 20000,
#     'melon': 15000,
#     'watermelon': 10000,
#     'grape': 18000
# }
# cart = []
# for i in range(4):
#     cart.append(input(f"O'zingiz hohlagan {i+1}-chi mevani kiriting: "))
#
# for order in cart:
#     if order in fruits:
#         print(f"{order}ning narxi - {fruits[order]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {order} yo'q.")
#
#
