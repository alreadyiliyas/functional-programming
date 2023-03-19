# Напишите функциональную и не функциональную функцию,
# и разберите отличие между ними. В качестве параметра можете использовать свое резюме.


# 1
def calculator(x, y, char):
    if char == '-':
        return x - y
    elif char == '+':
        return x + y
    elif char == '*':
        return x * y
    elif char == '/':
        return x / y


a = int(input("Input number 1:"))
b = int(input("Input number 2:"))
element = input("Input operation: ")
print(calculator(a, b, element))

# 2
def arrays_reverse(arr):
    tempList = []
    for element in range(len(arr)):
        tempList.append(arr[len(arr) - 1 - element])
    return tempList


size = int(input("Input arrays size: "))
arr = []
i = 0
while i < size:
    num = int(input("Input to arrays element: "))
    arr.append(num)
    i += 1
reversedArr = arrays_reverse(arr)
print(reversedArr)
