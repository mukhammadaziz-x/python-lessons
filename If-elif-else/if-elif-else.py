# age = int(input("How old are you?: "))
# if age <= 4:
#     print("You have free access.")
# elif age <= 12:
#     print("Your entrance fee is 5,000 so'm")
# else:
#     print("Your entrance fee is 10,000 so'm")

# clean code
# age = int(input("How old are you?: "))
# if age <= 4:
#     price = 0
# elif age <= 12:
#     price = 5000
# elif age < 65:
#     price = 10000
# else:
#     price = 8000
# print(f"Your entrance fee is {price} so'm.")

# and, or operators
# day = input("What day is it today?: ")
# if day.lower() == 'saturday' or day.lower() == 'sunday':
#     print("Today is a vacation.")
# else:
#     print(f"Today is a working day.")

# and
# day = input("What day is it today?: ")
# temperature = float(input("What is the temperature today?: "))
# if (day.lower() == 'saturday' or day.lower() == 'sunday') and temperature >= 30:
#     print("Let's go swimming!")
# elif (day.lower() == 'saturday' or day.lower() == 'sunday') and temperature < 30:
#     print(f"Today we're resting at home.")

# restaurant
# price = 15000
# tea = True
# salad = False
#
# if tea and salad:
#     price += 10000
# elif tea or salad:
#     price += 5000
#
# print(f"Total price is {price} so'm")

# check with only if
# price = 15000
# tea = True
# salad = False
# bread = True
# compote = True
# assorted_sweets = False
#
# if tea:
#     print("The customer bought tea.")
#     price += 3000
# if salad:
#     print("The customer bought salad.")
#     price += 5000
# if bread:
#     print("The customer bought bread.")
#     price += 2000
# if compote:
#     print("The customer bought compote.")
#     price += 5000
# if assorted_sweets:
#     print("The customer bought assorted sweets.")
#     price += 15000
#
# print(f"Total price is {price} so'm.")

# in operator
# menu = ['palov', 'kebab', 'narin', 'samsa', 'kazan kebab']
# print('manti' in menu)
# print('palov' in menu)

# not in operator
# menu = ['palov', 'kebab', 'narin', 'samsa', 'kazan kebab']
# print('manti' not in menu)
# print('palov' not in menu)

# order
# menu = ['palov', 'kebab', 'narin', 'samsa', 'kazan kebab']
# meal = input("What do you eat?: ")
# if meal.lower() in menu:
#     print("Order received!")
# else:
#     print("Unfortunately, we don't have such food.")

# order not in
# menu = ['palov', 'kebab', 'narin', 'samsa', 'kazan kebab']
# meal = input("What do you eat?: ")
# if meal.lower() not in menu:
#     print("Unfortunately, we don't have such food.")
# else:
#     print("Order received!")

# new restaurant with for and if
# menu = ['palov', 'kebab', 'narin', 'samsa', 'kazan kebab']
# orders = ['palov', 'samsa', 'kazan kebab']
#
# for food in orders:
#     if food in menu:
#         print(f"There is {food} on the menu.")
#     else:
#         print(f"Sorry, there is no {food} on the menu.")

# middle restaurant
# menu = ['palov', 'kebab', 'narin', 'samsa', 'kazan kebab']
# orders = ['palov', 'samsa', 'kazan kebab']
#
# if orders:
#     for food in orders:
#         if food in menu:
#             print(f"There is {food} on the menu.")
#         else:
#             print(f"Sorry, there is no {food} on the menu.")
# else:
#     print("Your cart is empty!")


# HOMEWORK
# 1. Assignment
# number = int(input("Enter an even number: "))
# if number % 2 == 0:
#     print("Thank you!")
# else:
#     print("This isn't an even number!")

# 2. Assignment
# age = int(input("How old are you?: "))
# price = 0
# if age <= 4 or age >= 60:
#     price += 0
# elif age < 18:
#     price += 10000
# elif age >= 18:
#     price += 20000
#
# print(f"Your entrance price is {price} so'm.")

# 3. Assignment
# products = ['bread', 'meat', 'rice', 'milk', 'egg', 'carrot', 'potato', 'tomato', 'onion', 'oil', 'salt']
# cart = []
# buy_product = int(input("Write down how many products you'll receive: "))
#
# for n in range(buy_product):
#     product = input(f"Write the name of the {n+1}-product you want to buy: ")
#     if product in products:
#         print(f"We have {product} in our store.")
#         cart.append(product)
#     else:
#         print(f"We don't have {product} in our store.")

# 4. Assignment
# products = ['bread', 'meat', 'rice', 'milk', 'egg', 'carrot', 'potato', 'tomato', 'onion', 'oil', 'salt']
# buy_product = int(input("Write down how many products you'll receive: "))
# available_products = []
# unavailable_products = []
#
# for n in range(buy_product):
#     product = input(f"Write the name of the {n+1}-product you want to buy: ").lower()
#     if product in products:
#         available_products.append(product)
#     else:
#         unavailable_products.append(product)
#
# if available_products:
#     print(f"The product you requested is available: {available_products}")
#
# if not unavailable_products:
#     print(f"All the products you requested are available in our store.")
# else:
#     print(f"The following products aren't available in our store: {unavailable_products}")
#
# order = input("Would you like to place an order? (yes/no): ")
# if order == 'yes':
#     print("Order received!")
#     available_products.clear()
# elif order == 'no':
#     print("Order canceled!")
# else:
#     print("You must answer (yes/no).")

# 5. Assignment
# users = ['muhammadaziz_', 'akmalxon1336', 'jamshidbek007', 'siddiqpaxan001', 'muhammadalivatan$20']
# choose = input("Enter your login: ")
# if choose in users:
#     print(f"Login is busy, choose a new login!")
# else:
#     print(f"Welcome {choose.title()}!")

# 6. Assignment
# num = int(input("Enter the integer you want: "))
# for n in range(2, 11):
#     if not (num % n):
#         print(f"The number {num} is divisible by {n} without a remainder.")