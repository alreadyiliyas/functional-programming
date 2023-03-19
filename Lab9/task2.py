# Напишите функцию в результате которая возвращает список, кортеж и словарь.
# Пример должен быть индивидуальным.
# Приведите свой пример с использованием функций Map, Filter и Reduce. Выясните отличия.

def returnAll():
    spisok = [2, 4, 6, 8]
    cortege = ("one", "two", "three", "four")
    dictionary = {
        "surname": "Ukenov",
        "name": "Iliyas",
        "age": 19,
        "gpa": 3.3
    }
    return spisok, cortege, dictionary


spisok, cortege, dictionary = returnAll()
print(spisok)
print(cortege)
print(dictionary)

firstArr = [1, 2, 3, 4]
secondArr = [3, 4, 5, 6]

powArr = list(map(pow, firstArr, secondArr))
print(powArr)

sumArr = list(map(lambda x, y: x + y, firstArr, secondArr))
print(sumArr)


def check_even(num):
    if num % 2 == 0:
        return True
    return False


num = [1, 2, 3, 4, 5, 6]

even_num = filter(check_even, num)

even_num = list(even_num)
print(even_num)

from functools import reduce


def reducer_func(el_prev, el):
    return el_prev + el


sum = reduce(reducer_func, [1, 2, 3, 4, 5])

print(sum)
