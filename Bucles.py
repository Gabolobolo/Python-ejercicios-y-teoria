#Teoria------------------------------------------------

counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

#break
    print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

# continue
print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

#Ejercicios-------------------------------------------------

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)
for letter in user_word:
    print(letter)


user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()
word_without_vowels = ""
for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter
print(word_without_vowels)


blocks = int(input("Ingresa la cantidad de bloques: "))
height = 0
blocks_used = 0
while blocks_used + (height + 1) <= blocks:
    height += 1
    blocks_used += height
print("La altura de la pirámide es:", height)


c0 = int(input("Ingresa un número natural: "))
if c0 <= 0:
    print("El número debe ser un entero positivo.")
else:
    steps = 0
    while c0 != 1:
        print(c0)  
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1
        steps += 1
    print(c0)
    print("Número de pasos:", steps)
    
