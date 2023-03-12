#1.	Напишите программу, используя 10 функции и методы, связанные со строками

import re

def FuncCount(text, find):
    print(f"Count: {text.count(find)}")
def Upper(text):
    print(f"Upper case: {text.upper()}")
def Lower(text):
    print(f"Lower case: {text.lower()}")
def Isalnum(text):
    print(f"Check text {text.isalnum()}")
def Delimetr(text, char):
    print(text.split(char))
def CheckEmail(email):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    res = re.fullmatch(pattern, email)
    if res:
        print('Успешно')
    else:
        print("Не успешно")
def DeleteSpace(text):
    print(f"Delete space: {text.strip()}")
def Fetch(text):
    pattern = "Hello"
    print(f"Found matches: {re.findall(pattern, text)}")
def Swap(text):
    old = "World"
    new = "Iliyas"
    print(f"Replace text: {text.replace(old, new)}")
def Join():
    string = ['Iliyas', 'Ukenov']
    space = " "
    print(f"Join text: {space.join(string)}")


text = input('Input text: ')
find = input('Input find count: ')
#Количество 1
FuncCount(text, find)
#Верхний регистр 2
Upper(text)

#Нижний 3
Lower(text)
#Проверка текста на все буквы или все числа 4
Isalnum(text)
#Поставить символ между текстом 5
char = input('Input delimetr: ')
Delimetr(text, char)
#Валидация 6
email = input('Input email: ')
CheckEmail(email)
#Удалить пробелы 7
DeleteSpace(text)
#Извлечь все совпадения из строки 8
Fetch(text)
#Замена 9
Swap(text)
#Объединение
Join()
