# Создайте кортеж-матрешку, в который поместите два элемента: целое
# число и вложенный кортеж, в который поместите еще два элемента: вещественное число и вложенный кортеж,
# в который поместите еще два элемента: комплексное число и вложенный кортеж, в который поместите еще два элемента: строку и пустой кортеж.
# Выведите на экран конечную строку.
cortege = (42, (3.14, (1 + 2j, ('Hello', ()))))

print(cortege[1][1][1][0])
