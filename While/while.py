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
num = 1
while num <= 5:
    print(num)
    num += 1

print("Kiritilgan sonning kvadratini chiqaruvchi dastur.")
question = "Istalgan son kiriting "
question += "(dasturni to'xtatish uchun 'exit' deb yozing): "
value = ''
while value != 'exit':
    value = input(question)
    if value != 'exit':
        print(float(value)**2)















