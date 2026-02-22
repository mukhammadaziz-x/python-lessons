def avto_info(company, model, color, box, year, price):
    avto = {
        'company': company,
        'model': model,
        'color': color,
        'box': box,
        'year': year,
        'price': price
    }
    return avto

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

print("\nSalonimizdagi avtolar: ")
for avto in avtolar:
    if avto['price']:
        price = avto['price']
    else:
        price = "Noma'lum"
    print(f"{avto['company'].title()} {avto['model'].title()}, {box} korobka. Narhi: {price}")

