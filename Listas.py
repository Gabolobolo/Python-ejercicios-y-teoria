#Teoria-----------------------------------------------------------

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  
numbers[0] = 111
print("Previo contenido de la lista:", numbers)  
numbers[1] = numbers[4]
print("Nuevo contenido de la lista:", numbers)
print("Longitud de la lista:", len(numbers))
del numbers[1]
print("\nLongitud de la nueva lista:", len(numbers))  
print("Nuevo contenido de la lista:", numbers)


numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)
numbers.append(4)
print(len(numbers))
print(numbers)
numbers.insert(0, 222)
print(len(numbers))
print(numbers)


my_list = [] 
for i in range(5):
    my_list.append(i + 1)
print(my_list)


my_list = []  
for i in range(5):
    my_list.insert(0, i + 1)
print(my_list)


my_list = [10, 1, 8, 3, 5]
total = 0
for i in range(len(my_list)):
    total += my_list[i]
print(total)


my_list = [10, 1, 8, 3, 5]
total = 0
for i in my_list:
    total += i
print(total)

my_list = [10, 1, 8, 3, 5]
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
print(my_list)


my_list = [8, 10, 6, 2, 4] 
swapped = True  
while swapped:
    swapped = False  
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)


my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)


#Ejercicios-----------------------------------------------------

hat_list = [1, 2, 3, 4, 5]  
hat_list[2] = int(input("Inserte un numero: "))
del hat_list[4]
print ("La longitud de la lista existente es: ", len(hat_list))
print(hat_list)


beatles = []
print("Paso 1:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)
for member in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(member)
print("Paso 3:", beatles)
del beatles[-1]
del beatles[-1]
print("Paso 4:", beatles)
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)
print("Los Fav", len(beatles))








