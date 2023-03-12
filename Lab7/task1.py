#1.	Напишите программу, используя минимум по 5 функции для работы со словарем (dict). В виде данных пусть каждый студент предложит свое резюме. И будет работать с этими данными.
dict = {
    "name": "Iliyas",
    "age": 19,
    "GPA": 3.3,
    "Subjects": ['Software Engeneering', 'Back-end', 'Mobile dev']
}

find = input("What do you want find? ")
print(dict[find])

add = input("What do you want to add? ")
x = add.split()
dict[x[0]] = x[1]
print(dict)

delete = input("What do you want to delete? ")
del dict[delete]

print(dict)

product = {
    "Orange": 20,
    "Apple": 18,
    "Banana": 23,
    "Mango": 32
}
sum = 0
for value in product.values():
    sum += value
print(f"Sum of product: {sum}")

text = input("Counter words: ")
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():
    print(word, ":", count)
