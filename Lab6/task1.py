# Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Также заполните второй кортеж числами от -5 до 0. Для заполнения кортежей числами напишите одну функцию.
# Объедините два кортежа с помощью оператора +, создав тем самым третий кортеж.
# С помощью метода кортежа count() определите в нем количество нулей.
# Выведите на экран третий кортеж и количество нулей в нем.

def inputCortege(cortege):
    i = 0
    print(f"Enter cortege")
    while (i <= 5):
        values = int(input("Enter values: "))
        cortege = (*cortege, values)
        i += 1
    return cortege

def sumCortege(x, y):
    return x + y

cortege1 = ()
cortege2 = ()
cortege3 = ()
cortege1 = inputCortege(cortege1)
cortege2 = inputCortege(cortege2)
cortege3 = sumCortege(cortege1, cortege2)
print(cortege1)
print(cortege2)
print(cortege3.count(0))
