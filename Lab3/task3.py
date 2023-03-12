# Используйте функции randint() randrange() random() enumerate()  в своей программе
import random

def casino():
    name = input()
    bid = int(input())

    prize = random.randint(1, 6)
    if bid == prize:
        print("выиграш", "выпало: ", prize)
    else:
        print("в след раз", "выпало: ", prize)


casino()
