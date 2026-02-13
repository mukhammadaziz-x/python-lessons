# guests = ['Muhammadumar', 'Siddiq', 'Asadulloh', 'Muhammadali', 'Yahyoxon']
# # for guest in guests:
# #     print(guest)
#
# for guest in guests:
#     print(f"Dear {guest}, we invite you to a luncheon on December 20th.")
#     print("Sincerely, the Palonchiev family.")
# print(guests)
#
# numbers = list(range(1, 11))
# for num in numbers:
#     print(f"The square of {num} is {num**2}")
#
# square_of_nums = []
# for num in numbers:
#     square_of_nums.append(num**2)
#
# print(numbers)
# print(square_of_nums)
#
# # for and input()
# friends = []
# print("Who are your 5 closest friends?")
# for n in range(5):
#     friends.append(input(f"Enter your {n+1}-friend's name: "))
# print(friends)

# HOMEWORK
# 1. Assignment
names = ['Muhammadumar', 'Siddiq', 'Asadulloh', 'Muhammadali', 'Yahyoxon']
for name in names:
    print(f"What's up {name}?")
print(f"Code repeated {len(names)} times.")

# 2. Assignment
numbers = list(range(9, 100, 2))
for num in numbers:
    print(f"The square of {num} is {num**2}")

# 3. Assignment
movies = []
for mov in range(5):
    movies.append(input(f"Enter your {mov+1} favorite movie: "))
print(movies)

# 4. Assignment
meet_people = []
how_many = int(input("How many people did you see/talk to today?: "))
for p in range(how_many):
    meet_people.append(input(f"Name of the {p+1}-person you met/talked to today: "))

print(how_many)
print(meet_people)

