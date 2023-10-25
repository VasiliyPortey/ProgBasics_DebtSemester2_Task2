from random import randint

def twoToOne(list1, list2):
    i = 0
    while i<len(list2):
        list1.append(list2[i])
        i+=1
    return list1

length1 = int(input("Введите длину первого списка: "))
list1 = []
for i in range(length1):
    list1.append(randint(-10, 10))
print("\nПервый список: \n", list1)
length2 = int(input("\nВведите длину второго списка: "))
list2 = []
for i in range(length2):
    list2.append(randint(-10, 10))
print("\nВторой список: \n", list2)
print("Конечный список: ", twoToOne(list1, list2))
