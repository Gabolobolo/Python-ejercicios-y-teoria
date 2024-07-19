#Teoria----------------------------------------------------------

print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")


anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")


anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "al cuadrado es", something)


print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

#Ejercicios------------------------------------------------------

num1= float(input("Ingresa el primer numero: "))
num2= float(input("Ingresa el segundo numero: "))
print("\nLa suma es: " , (num1 + num2))
print("\nLa resta es: " , (num1 - num2))
print("\nLa multiplicacion es: " , (num1 * num2))
print("\nLa division es: " , (num1 / num2))
print("\n¡Eso es todo, amigos!")


x = float(input("Ingresa el valor para x: "))
y = (1/(x+(1/(x+(1/(x+(1/x)))))))
print("y =", y)


hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura 
hour = hour + mins // 60 
mins = mins % 60 
hour = hour % 24 
print(hour, ":", mins, sep='')
