# cars = ['bmw', 'volvo', 'volkswagen', 'general motors', 'tesla', 'byd', 'audi', 'jaguar', 'bentley', 'hyundai', 'honda']
# # cars.sort()
# # print(cars)
# # cars.sort(reverse=True)
#
# print(sorted(cars, reverse=True))
from xxsubtype import bench

# sorted
# ages = [11, 12, 34, 65, 76, 84, 100]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))
#
# # reverse()
# fruits = ['apple', 'banana', 'melon', 'kiwi', 'watermelon']
# fruits.reverse()
# print(fruits)
#
# # len()
# print(f"Elementlar soni: {len(fruits)}")

# range()
# numbers = list(range(1, 11))
# print(numbers)

# to step
# even_num = list(range(0, 11, 2))
# odd_num = list(range(1, 11, 2))
#
# print(f"Even numbers: {even_num}")
# print(f"Odd numbers: {odd_num}")

# simple operations on a numerical list
# prices = [12000, 18000, 23546, 9800, 5600, 9934, 32874]
# cheap = min(prices)
# expense = max(prices)
# total = sum(prices)
#
# print(f"The cheapest price {cheap}. The most expensive {expense}. Total price {total}.")

# slicing list
# my_cars = cars[0:3]
# print(my_cars)
#
# print(cars[5:9])
# print(cars[:4])
# print(cars[5:])
#
# numberss = [1,2,3,4,5,6,7]
# numbers2 = numberss
# numbers2.append(121)
# numbers2.append(-2123)
# print("This is list of numbers:", numberss)
# print("This is list of numbers:", numbers2)
#
# numbers2 = numberss[:]
# numbers2.append(2321111)
# numbers2.append(-10)
# print(numbers2)
# print(numberss)

# TUPLE
# towards = (20, 30, 55.2)
# print(towards)
#
# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# toys[3] = 'electrobus'
# print(toys)

# edit to list
# toys = list(toys)
# toys.remove('lizard')
# toys.append('mouse')
# toys.insert(4, 'apple')
# toys[3] = 'mcqueen'
# toys = tuple(toys)
# print(toys)

# HOMEWORK
# countries = ['Afghanistan', 'Albania', 'Algeria', 'Australia', 'Bangladesh', 'Barbados', 'Bavaria', 'Brazil', 'Canada', 'China', 'Columbia', 'Croatia']
# print(f"Length of countries: {len(countries)}")
# print(sorted(countries, reverse=True))
# print(countries)
#
# countries.reverse()
# print(countries)
#
# countries.sort()
# print(countries)
#
# countries.sort(reverse=True)
# print(countries)
#
# numbers = list(range(120, 1200))
# print(numbers)
#
# total_nums = sum(numbers)
# print(total_nums)
#
# huge_num = max(numbers)
# low_num = min(numbers)
# print(huge_num - low_num)
#
# print(len(numbers))
#
# print(numbers[:20])
# print(numbers[590:620])
# print(numbers[-20:])

# Meals
meals = ['hamburger', 'donary', 'lavash', 'hotdog', 'pizza', 'egg with sausages', 'omelette']
breakfast = meals[:]
print(breakfast)

breakfast.remove('pizza')
breakfast.remove('lavash')
breakfast.remove('hotdog')
breakfast.remove('donary')
breakfast.remove('hamburger')

breakfast.append('milk and cookies')
breakfast.insert(2, 'bread with oil')
breakfast.append('cottage cheese with strawberry')
breakfast.insert(4, 'cake with chocolate')
breakfast.insert(5, 'bread and cream')
# print(breakfast)

breakfast = tuple(breakfast)
print(breakfast)