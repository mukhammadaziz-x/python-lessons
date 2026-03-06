# Working with files
# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close() # Don't recommend

# Correct method
# with open('pi.txt') as file:
#     pi = file.read()
#
# print(pi)
# print(type(pi))
#
#
# pi = pi.rstrip()
# pi = pi.replace('\n', '')
# pi = float(pi)
# print(type(pi))

filename = 'data/students.py'
# with open(filename) as file:
#     for line in file:
#         print(line)

with open(filename) as file:
    students = file.readlines()

print(students)

students = [student.rstrip() for student in students]
print(students)