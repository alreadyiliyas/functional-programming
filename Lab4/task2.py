#2.	Напишите программу, в которой предлагается вводить учащихся различных груп,
# посещающих секции по программированию. Требуется упорядочить список по возрастанию классов.
# Распечатать список фамилий и классов.

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
