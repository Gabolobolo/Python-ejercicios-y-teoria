#Teoria-----------------------------------------------------------

def message(number):
    print("Ingresa un número:", number)
message(1)

def message(what, number):
    print("Ingresa", what, "número", number)
message("teléfono", 11)

def introduction(first_name, last_name="Smith"):
     print("Hola, mi nombre es", first_name, last_name)
introduction(first_name="Guillermo")


def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return
    print("Feliz a;o nuevo!")
happy_new_year()

def boring_function():
    return 123
x = boring_function()
print("La función boring_function ha devuelto su resultado. Es:", x)


def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2)) #imprime true
print(strange_function(1))#imprime NONE (Error dentro de la funcion)


def strange_list_fun(n):
    strange_list = []
    for i in range(0, n):
        strange_list.insert(0, i)
    return strange_list
print(strange_list_fun(5))


#Ejercicios -------------------------------------------------------


def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    #Comprueba si el año es bisiesto
def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res
    #Comprueba los meses
def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None
print(day_of_year(2000, 12, 31))


def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons
def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    liters = 3.785411784
    return liters / km100
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))







