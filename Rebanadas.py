#Teoria ---------------------------------------------------------

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[0:3]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
#imprime 10,8,6

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)
#imprime 4,2

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
#imprime 10,4,2

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)
#imprime[]

my_list = [8, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]
print(largest)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")


board = []
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
#crea una matriz 8*8
board = [[EMPTY for i in range(8)] for j in range(8)]





#Ejercicios-------------------------------------------------------

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []
for number in my_list:
    if number not in unique_list:
        unique_list.append(number)
print("Lista original:", my_list)
print("Lista sin repeticiones:", unique_list)




