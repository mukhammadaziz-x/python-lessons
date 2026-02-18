print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
friends = []
n = 1
while True:
    question = f"{n}-do'stingizni ismini kiriting: "
    name = input(question)
    friends.append(name)
    repeat = input("Yana ism qo'shishni hohlaysizmi (ha/yo'q): ")
    n += 1
    if repeat != 'ha':
        break

for friend in friends:
    print(friend.title())

