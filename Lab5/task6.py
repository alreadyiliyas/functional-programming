# Напишите функцию, показывающую, отсортирован ли
# переданный ей в качестве параметра список (по возрастанию или
# убыванию). Функция должна возвращать True, если список
# отсортирован, и False в противном случае. В основной программе
# запросите у пользователя последовательность чисел для списка, после
# чего выведите сообщение о том, является ли этот список
# отсортированным изначально.


import random

list1 = []
list2 = []
size = 0
while True:
    x = int(input('Input: '))
    if x == 0:
        break
    list1.append(x)
    list2.append(x)
    size += 1
list2.sort()
count = 0
for i in range(size):
    if list1[i] == list2[i]:
        count += 1


if count == size:
    print('List sorted')
else:
    print('No')
