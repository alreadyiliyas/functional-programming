# Напишите программу которая возвращает список. Заранее
# подготовьте список предметов и оценок учащихся. Когда вы вводите
# имя учащегося, то должны отображаться оценки этого учащегося.

students = []


while True:
    surname = input("Enter surname (or 'q' to quit): ")
    if surname == 'q':
        break

    student_class = int(input("Enter class: "))
    student_group = input("Enter group: ")
    i = 0
    student_rating = []
    while i < 3:
        student_Rating = int(input("Enter rating: "))
        student_rating.append(student_Rating)
        i += 1

    students.append({"surname": surname, "class": student_class, "group": student_group, "rating": student_rating})

findStudent = input("Найти студента: ")


for student in students:
    if student["surname"] == findStudent:
        print(f"{student['surname']}: Class {student['class']}, Group {student['group']}, Rating: {student['rating']}")
    else:
        print("Error")
