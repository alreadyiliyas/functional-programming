#2)	Строковый метод isdigit() проверяет, состоит ли строка только из цифр.
# Напишите программу, которая запрашивает с ввода два целых числа и выводит их сумму.
# В случае некорректного ввода программа не должна завершаться с ошибкой,
# а должна продолжать запрашивать числа. Обработчик исключений try-except использовать нельзя.

while True:
    num1 = input("Input num1: ")
    if num1.isdigit():
        break
    print("Error")
while True:
    num2 = input("Input num2: ")
    if num2.isdigit():
        break
    print("error")

print(int(num1) + int(num2))
