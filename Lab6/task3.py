# Общий объем расходов. Разработайте программу, которая подсчитает ваши расходы за каждый день недели.
# Расходы по следующим категориям (транспортные расходы, обед, и т.д.)
# Суммы должны быть сохранены в списке. Примените цикл, чтобы вычислить общий объем расходов за неделю и показать результат.

list = []
id = 1
size = int(input("Size: "))

while id <= size:
    food = input("Food: ")
    transport = input("Transport: ")
    balance = input("Balance: ")
    list.append({"id": id, "food": food, "transport": transport, "balance": balance})
    id += 1

sumFood = 0
sumTransport = 0
sumBalance = 0

for values in list:
    sumFood += int(values["food"])
    sumTransport += int(values["transport"])
    sumBalance += int(values["balance"])
print(f"Sum food: {sumFood}, Sum transport: {sumTransport}, Sum balance: {sumBalance}")
