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
# READ
# pi = pi.rstrip()
# pi = pi.replace('\n', '')
# pi = float(pi)
# print(type(pi))

# filename = 'data/students.py'
# with open(filename) as file:
#     for line in file:
#         print(line)

# with open(filename) as file:
#     students = file.readlines()
#
# print(students)

# students = [student.rstrip() for student in students]
# print(students)


# WRITE
# filename = 'pi.txt'
# name = 'Muhammadaziz Xabibullayev'
# b_year = 2006
# with open(filename, 'w') as file:
#     file.write(name + '\n')
#     file.write(str(b_year) + '\n')

# APPEND
# filename = 'pi.txt'
# with open(filename, 'a') as file:
#     file.write('Muhammadaziz Xabibullayev')
#     file.write('2006')
#     file.age('20')

