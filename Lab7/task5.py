# Составьте словарь «График отпусков» для специалиста отдела кадров. По известному графику отпусков научитесь определять,
# у кого отпуск в заданном месяце.
# В первой строчке записано целое число – количество сотрудников. В следующих N строчках записана информация о дате их отпуска.
# Каждая строчка состоит из трёх частей, разделённых пробелом – фамилии сотрудника, дня и месяца его отпуска.

# Создаем пустой словарь для графика отпусков
vacation_schedule = {}

# Вводим количество сотрудников
n = int(input())

# Вводим информацию о дате отпуска для каждого сотрудника
for i in range(n):
    name, day, month = input().split()
    # Если месяц еще не встречался, добавляем его в словарь и записываем сотрудника
    if month not in vacation_schedule:
        vacation_schedule[month] = [name]
    # Если месяц уже есть в словаре, добавляем сотрудника в список
    else:
        vacation_schedule[month].append(name)

# Вводим запрос на месяц отпуска
requested_month = input()

# Если месяц есть в словаре, выводим список сотрудников
if requested_month in vacation_schedule:
    print(*vacation_schedule[requested_month])
# Если месяца нет в словаре, выводим сообщение об отсутствии отпусков
else:
    print("Никто не идет в отпуск в указанный месяц")
