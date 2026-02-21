def bahola(names):
    grades = {}
    while names:
        name = names.pop()
        grade = input(f"{name.title()} ismli talabani baholang: ")
        grades[name] = int(grade)
    return grades

students = ['ali', 'vali', 'akmalxon', 'siddiq', 'muhammadaziz']
grades = bahola(students[:])
print(grades)
print(students)