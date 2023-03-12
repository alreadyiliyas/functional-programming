# Вводятся имена студентов в одну строчку через пробел. На их основе формируется кортеж.
# Отобразите на экране все имена из этого кортежа, которые содержат фрагмент "ва".
# Имена выводятся в одну строку через пробел.

names = input("Enter names: ")

name = names.split()

cortege = tuple(name)
for name in cortege:
    i = 0
    size = len(name)
    while i < size:
        if name[i] == 'в' and name[i+1] == 'а':
            print(name)
        i += 1
