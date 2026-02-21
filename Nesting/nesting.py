# Lug'atlar ichida ro'yxatlar

car0 = {
    'model': 'lacetti',
    'color': 'oq',
    'year': 2018,
    'price': 13000,
    'km': 50000,
    'box': 'avtomat'
}

car1 = {
    'model': 'nexia 3',
    'color': 'qora',
    'year': 2015,
    'price': 9000,
    'km': 89000,
    'box': 'avtomat'
}

car2 = {
    'model': 'gentra',
    'color': 'qizil',
    'year': 2019,
    'price': 13000,
    'km': 50000,
    'box': 'avtomat'
}
car = car0
print(f"{car['model'].title()}, "
      f"{car['color']} rang, "
      f"{car['year']}-yil, {car['price']}$")

car = car1
print(f"{car['model'].title()}, "
      f"{car['color']} rang, "
      f"{car['year']}-yil, {car['price']}$")

car = car2
print(f"{car['model'].title()}, "
      f"{car['color']} rang, "
      f"{car['year']}-yil, {car['price']}$")

# clean code
cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['color']} rang, "
          f"{car['year']}-yil, {car['price']}$")

print(cars[2]['color'])
print(cars[1]['model'])
print(cars[0]['price'])

print(f"{cars[2]['color'].title()} "
      f"{cars[2]['model']}")

malibus = []
for i in range(10):
    new_car = {
        'model': 'malibu',
        'color': None,
        'year': 2026,
        'price': None,
        'km': 0,
        'box': 'avto'
    }
    malibus.append(new_car)

for i in malibus[:3]:
    i['color'] = 'qizil'

for i in malibus[3:6]:
    i['color'] = 'black'

for i in malibus[6:]:
    i['color'] = 'white'
    i['box'] = 'mexanika'

for i in malibus:
    print(i)

for malibu in malibus:
    if malibu['box'] == 'avto':
        malibu['price'] = 40000
    else:
        malibu['price'] = 35000

for i in malibus:
    print(i)

programmers = {
    'ali': ['python', 'c++'],
    'vali': ['html', 'css', 'js'],
    'hasan': ['php', 'sql'],
    'husan': ['python', 'php'],
    'maryam': ['c++', 'c#']
}

for name, langs in programmers.items():
    print(f"{name.title()} quyidagi dasturlash tillarini biladi: ")
    for lang in langs:
        print(lang.upper())

for name, langs in programmers.items():
    print(f"{name.title()} quyidagi dasturlash tillarini biladi: ")
    for lang in langs:
        print(f"{lang.upper()}", end='')

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

# HOMEWORK
# 1. Assignment
mashhur_shaxs0 = {
    'name': 'imom al-buxoriy',
    'b_day': 1100,
    'major': 'hadith',
    'books': 'jome us-sahih'
}

mashhur_shaxs1 = {
    'name': 'enshteyn',
    'b_day': 1890,
    'major': 'phisics',
    'books': 'einstein book'
}

mashhur_shaxs2 = {
    'name': 'leonardo da-vinchi',
    'b_day': 1890,
    'major': 'phisics',
    'books': 'einstein book'
}

mashhur_shaxs3 = {
    'name': 'stive jobs',
    'b_day': 1970,
    'major': 'computer engineer',
    'books': 'stive jobs'
}

literature = [mashhur_shaxs0, mashhur_shaxs1, mashhur_shaxs2, mashhur_shaxs3]
for celebriry in literature:
    print(f"{celebriry['name'].title()} {celebriry['b_day']}-yilda tug'ilgan. "
          f"U {celebriry['major'].title()} sohasida olim bo'lgan. "
          f"U {celebriry['books']} kitobini yozgan.")

# 2. Assignment
for celebrity in literature:
    print(f"{celebrity['name'].title()} {celebrity['books'].title()} asarini yozgan.")

# 3. Assignment
dostim = {
    'name': 'Siddiq',
    'b_day': 2007,
    'major': 'AI engineer',
}

akam = {
    'name': 'Otabek',
    'b_day': 2003,
    'major': 'Flutter developer'
}

ukam = {
    'name': 'Muhammadyusuf',
    'b_day': 2008,
    'major': 'Business analytic'
}
tanishlar = [dostim, ukam, akam]
movies = []

print(f"3 ta eng sevimli kinoingizni yozing:")
for n in range(3):
    movies.append(input(f"{n+1}-kino: ").lower())

for tanish in tanishlar:
    tanish['favorite_movies'] = movies

for tanish in tanishlar:
    print(f"{tanish['name'].title()}ning sevimli kinolari:")
    for movie in tanish['favorite_movies']:
        print(movie.capitalize())

# 4. Assignment
countries = {
    'uzbekistan': {
        'capital': 'tashkent',
        'population': 38_000_000,
        'currency': "so'm",
        'language': 'uzbek'
    },
    'turkiya': {
        'capital': 'istanbul',
        'population': 85_000_000,
        'currency': "lira",
        'language': 'turk'
    },
    'yaponiya': {
        'capital': 'tokio',
        'population': 125_000_000,
        'currency': "iyena",
        'language': 'yapon'
    },
    'germaniya': {
        'capital': 'berlin',
        'population': 83_000_000,
        'currency': "yevro",
        'language': 'nemis'
    }
}

for country, info in countries.items():
    print(f"{country.title()}ning poytaxti {info['capital'].title()}. "
          f"Aholi soni {info['population']} va pul birligi {info['currency']}. "
          f"Bu davlatning tili {info['language'].title()}.")

query = input("Davlat nomini kiritib, u haqida ma'lumot oling: ").lower()

if query in countries:
    info = countries[query]
    print(f"{query.title()}ning poytaxti {info['capital'].title()}. "
          f"Aholi soni {info['population']} va pul birligi {info['currency']}. "
          f"Bu davlatning tili {info['language'].title()}.")
else:
    print(f"Bizda {query} davlati haqida ma'lumot yo'q.")

# PRACTICE
# 1. Assignment
team = []
total_price = 0

for i in range(5):
    player = {
        'name': 'Karim',
        'position': 'defender',
        'rating': None,
        'price': None
    }
    team.append(player)

for player in team[:2]:
    player['position'] = 'attacker'
    player['price'] = 100_000_000

for player in team[2:]:
    player['price'] = 50_000_000
    player['position'] = 'defender'

for player in team:
    if player in team:
        total_price += player['price']

print(total_price)

# 2. Assignment
restaurant_menu = {
    'palov': {
        'price': 45000,
        'ingredients': ["go'sht", 'sabzi', 'guruch', "yog'"]
    },
    'kebab': {
        'price': 20000,
        'ingredients': ["go'sht", 'pomidor', 'limon', "qo'y yog'i"]
    },
    'mastava': {
        'price': 45000,
        'ingredients': ["go'sht", 'guruch', 'sabzi', 'kartoshka', "bulg'or qalampir"]
    },
    'narin': {
        'price': 45000,
        'ingredients': ["go'sht", 'qazi', 'hamr', 'ziravor']
    }
}

query = input("Taom kiriting: ").lower()

if query in restaurant_menu:
    print(f"Siz so'ragan {query.title()}ning narxi {restaurant_menu[query]['price']} so'm.")
    print(f"{query.title()}ning tarkibida:")
    for ing in restaurant_menu[query]['ingredients']:
        print(ing.capitalize(), end=' - ')
else:
    print("Afsuski, bizda bunday taom yo'q.")

# 3. Assignment
library = {
    'badiiy': [{
        'name': "o'tkan kunlar",
        'author': 'abdulla qodiriy',
        'page': 560
    }],
    'ilmiy': [{
        'name': "qora pul",
        'author': 'george armstrong',
        'page': 380
    }]
}

for janr, books in library.items():
    print(f"{janr.title()}:")
    for book in books:
        print(f'"{book["name"].capitalize()}", muallifi: {book["author"].title()}, {book["page"]} bet.')

