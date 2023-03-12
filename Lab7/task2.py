# В первой строке содержится число N — число элементов в словаре. Дан список (словарь) стран и рек, протекающих в каждой стране. Затем даны названия рек (в виде списка). Выполните задания:
# 1)	Для   каждой   реки   укажите,    в   какой    стране    она    протекает.
# 2)	Проверьте,   есть    ли    введенное    название    реки    в    словаре
# (вывести есть или нет)
# 3)	Добавьте новую пару страна-река в словарь.
n = int(input("Size of dict: "))

country_river = {
    "Africa": "Amazonka",
    "Russian": "Enisei",
    "Kazakhstan": "Oral"
}

nameOfRiver = ["Amazonka", "Nil", "Volga"]

#1
i = 0
for value in country_river.values():
    if value != nameOfRiver[i]:
        print("no")
    else:
        print("yes")
    i+=1

#2
add = input("Add country: river").split()
country_river[add[0]] = add[1]

add = input("Add country: river").split()
country_river[add[0]] = add[1]

print(country_river)
