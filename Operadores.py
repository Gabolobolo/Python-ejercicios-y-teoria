#Teoria----------------------------------------------

var = 0  
print(var == 0)
var = 1 
print(var == 0)


var = 0  
print(var != 0) #no igual a
var = 1 
print(var != 0)


centigrade_outside >= 0.0  
current_velocity_mph <= 85

number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
largest_number = max(number1, number2, number3)
print("El número más grande es:", largest_number)


#Ejercicios---------------------------------------------------

numero = int(input("Ingresa un número: "))
print(numero >= 100)


name = input("Introduce el nombre de la flor: ")
if name == "ESPATIFILIO":
    print("Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!")
elif name == "espatifilo":
    print("No, ¡quiero un gran ESPATIFILIO!")
else:
    print("¡ESPATIFILIO!, ¡No", name + "!")


ingreso=float(input("Ingrese su sueldo: "))
if ingreso<=85528:
    impuesto=((ingreso*18)/100) - 556.02
else:
    impuesto= (14839.02)+ ((ingreso-85528*32)/100)

if tax < 0.0:
	tax = 0.0
tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")


year = int(input("Introduce un año: "))
if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if year % 4 != 0:
		print("Año Común")
	elif year % 100 != 0:
		print("Año Bisiesto")
	elif year % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")






