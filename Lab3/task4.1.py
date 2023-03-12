#Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
a = int(input())
b = int(input())
while a <= b:
    print(a)
    a += 1
