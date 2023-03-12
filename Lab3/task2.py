# Используя функцию range() сделать список. в функцию range() введите данные с
# разными типами и выведите на экран в разных примерах.
list = []
list.append("Ilias")
list.append("Ukenov")
list.append(19)
for i, value in enumerate(list, 1):
    print(f'{i}: {value} ')
