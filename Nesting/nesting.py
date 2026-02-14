# Lug'atlar ichida ro'yxatlar
#
# car0 = {
#     'model': 'lacetti',
#     'color': 'oq',
#     'year': 2018,
#     'price': 13000,
#     'km': 50000,
#     'box': 'avtomat'
# }
#
# car1 = {
#     'model': 'nexia 3',
#     'color': 'qora',
#     'year': 2015,
#     'price': 9000,
#     'km': 89000,
#     'box': 'avtomat'
# }
#
# car2 = {
#     'model': 'gentra',
#     'color': 'qizil',
#     'year': 2019,
#     'price': 13000,
#     'km': 50000,
#     'box': 'avtomat'
# }
# car = car0
# print(f"{car['model'].title()}, "
#       f"{car['color']} rang, "
#       f"{car['year']}-yil, {car['price']}$")
#
# car = car1
# print(f"{car['model'].title()}, "
#       f"{car['color']} rang, "
#       f"{car['year']}-yil, {car['price']}$")
#
# car = car2
# print(f"{car['model'].title()}, "
#       f"{car['color']} rang, "
#       f"{car['year']}-yil, {car['price']}$")

# clean code
# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['color']} rang, "
#           f"{car['year']}-yil, {car['price']}$")
#
# print(cars[2]['color'])
# print(cars[1]['model'])
# print(cars[0]['price'])

# print(f"{cars[2]['color'].title()} "
#       f"{cars[2]['model']}")

# malibus = []
# for i in range(10):
#     new_car = {
#         'model': 'malibu',
#         'color': None,
#         'year': 2026,
#         'price': None,
#         'km': 0,
#         'box': 'avto'
#     }
#     malibus.append(new_car)
#
# for i in malibus[:3]:
#     i['color'] = 'qizil'
#
# for i in malibus[3:6]:
#     i['color'] = 'black'
#
# for i in malibus[6:]:
#     i['color'] = 'white'
#     i['box'] = 'mexanika'

# for i in malibus:
#     print(i)

# for malibu in malibus:
#     if malibu['box'] == 'avto':
#         malibu['price'] = 40000
#     else:
#         malibu['price'] = 35000
#
# for i in malibus:
#     print(i)

# programmers = {
#     'ali': ['python', 'c++'],
#     'vali': ['html', 'css', 'js'],
#     'hasan': ['php', 'sql'],
#     'husan': ['python', 'php'],
#     'maryam': ['c++', 'c#']
# }
#
# for name, langs in programmers.items():
#     print(f"{name.title()} quyidagi dasturlash tillarini biladi: ")
#     for lang in langs:
#         print(lang.upper())
#
# for name, langs in programmers.items():
#     print(f"{name.title()} quyidagi dasturlash tillarini biladi: ")
#     for lang in langs:
#         print(f"{lang.upper()}", end='')

collegues = {
    'ali': {
        'surname': 'valiyev',
        'b_day': 2005,
        'malumot': 'oliy',
        'languages': ['python', 'c++']
    },
    'vali': {
        'surname': 'valiyev',
        'b_day': 1999,
        'malumot': 'orta-maxsus',
        'languages': ['sql', 'php']
    },
    'olim': {
        'surname': 'husanov',
        'b_day': 1985,
        'malumot': 'maxsus',
        'languages': ['c#', 'ruby']
    }
}

for name, info in collegues.items():
    print(f"{name.title()} {info['surname'].title()}, {info['b_day']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}."
          f"Quyidagi dasturlash tillarini biladi: ")
    for lang in info['languages']:
        print(lang.upper())
