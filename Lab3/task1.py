# Написать программу используя цикл for и while.
height = int(input('Высота пирамиды: '))
for j in range(1, height + 1):
    for i in range(height * 2 + 1):
        if i == height:
            print('*' * (j * 2 - 1), end="")
            height -= 1
        else:
            print(' ', end="")
    print()

element = int(input("Sum of elements: "))
sum = 0
len = 0
while element != 0:
    sum += element
    len += 1
    element = int(input())
print(sum / len)
