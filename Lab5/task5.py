# Для выигрыша главного приза необходимо, чтобы шесть
# номеров на лотерейном билете совпали с шестью числами, выпавшими
# случайным образом в диапазоне от 1 до 49 во время очередного тиража.
# Напишите программу, которая будет случайным образом подбирать
# шесть номеров для вашего билета. Убедитесь в том, что среди этих
# чисел не будет дубликатов. Выведите номера билетов на экран по
# возрастанию.

import random

listPerson = []
listRandom = []
size = 6
for i in range(size):
    x = int(input("Input: "))
    listPerson.append(x)

exclusiveNum = set(range(1, 50))
listRandom = sorted(random.sample(exclusiveNum, size))
count = 0
for i in range(size):
    for j in range(size):
        if (listRandom[i] == listPerson[j]):
            count += 1
listRandom.sort()
listPerson.sort()
print(listPerson)
print(listRandom)
print(f"Одинаковых чисел: {count}")

