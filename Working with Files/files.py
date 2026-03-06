# Working with files
# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close() # Don't recommend

# Correct method
with open('pi.txt') as file:
    pi = file.read()

print(pi)

