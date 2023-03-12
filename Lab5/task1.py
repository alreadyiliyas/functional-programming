# Напишите программу, в которой предлагается вводить учащихся
# различных групп, посещающих секции по разным предметам. Требуется
# упорядочить список по различным категориям. Вывести результат на
# экран.
students = []

while True:
    surname = input("Enter surname (or 'q' to quit): ")
    if surname == 'q':
        break

    student_class = int(input("Enter class: "))
    student_group = input("Enter group: ")
    students.append({"surname": surname, "class": student_class, "group": student_group})

students.sort(key=lambda x: x["class"])

for student in students:
    print(f"{student['surname']}: Class {student['class']}, Group {student['group']}")
