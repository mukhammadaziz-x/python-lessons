def avto_info(company, model, color, box, year, price):
    """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {
        'company': company,
        'model': model,
        'color': color,
        'box': box,
        'year': year,
        'price': price
    }
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info() funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta bitta qo'shish funksiyasi"""
    print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
    avtolar = []
    while True:
        print("Quyidagi ma'lumotlarni kiriting")
        company = input("Kompaniyani kiriting: ")
        model = input("Modelni kiriting: ")
        color = input("Rangini kiriting: ")
        box = input("Karobkasini kiriting: ")
        year = input("Ishlab chiqarilgan yilni kiriting: ")
        price = input("Narhini kiriting: ")

        avtolar.append(avto_info(company, model, color, box, year, price))

        result = input("Yana ma'lumot kiritasizmi? (yes/no): ")
        if result == 'no':
            break
        return avtolar

def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['color'].title()} {avto_info['company'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['box']} korobka, "
          f"{avto_info['year']}-yil, ${avto_info['price']}.")


