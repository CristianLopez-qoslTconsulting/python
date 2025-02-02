# ========== Variables ==========

# string
variable_string = "Mi String"
print(variable_string)

# int
variable_int = 5
print(variable_int)

#float
variable_double = 5.5
print(variable_double)

# boolean
variable_boolean = True
print(variable_boolean)

# concatenacion de variables
print(variable_boolean,variable_int,variable_string,variable_double)


# modificar variables
print("variables modificadas")
variable_string = "string 2"
variable_int = 30
variable_double = 55.1
variable_boolean = False

print(variable_int,variable_double,variable_string,variable_boolean)

# =============== Manejo de indices de cadena ===============

cadena1 = "Hola mundo"

#primer caracter
primer_caracter = cadena1[0]
print(primer_caracter)

# ultimo caracter
ultimo_caracter = cadena1[9]
print (ultimo_caracter)

# =============== caracteres especiales ===============

print("Hola \nMundo") #\n salto de linea
print("\tHola Mundo") # \t agraga 1 tabulacion
print("\u00A9")  #  imprime: © (caracteres Unicode)
print("\U0001F600")  # imprime: emoticono de cara sonriente (caracteres Unicode)
print("Hola\bMundo")  # imprime: HolMundo | \b elimina el carácter anterior
print("12345\rabc")  # Imprime 'abc45' sobreescribiendo el '123' inicial


# =============== f string ===============
nombre = "cristian"
edad = 21

mensaje = f'Hola me llamo {nombre} y tengo {edad} años'
print(mensaje)

#  =============== metodo format ===============

mensaje = "Hola me llamo {} y tengo {} años".format(nombre,edad)
print (mensaje)

#===============  upper('cadena') y lower('cadena') ===============

# forma 1
cadena_Mayusculas = mensaje.upper()
print (f"Cadena en mayusculas: {cadena_Mayusculas}")

# forma 2
print (f"Cadena en mayusculas: {cadena_Mayusculas.lower()}")

# ===============  strip('cadena') ===============
cadena2 = " Me llamo cristian "
print(f"cadena con espacios: {cadena2}")
print(f"cadena sin espacios {cadena2.strip()}")

# Largo de una cadena len('cadena')

cadena3 = "hola mundo!"
largo_cadena = len(cadena3)
print(f"Cadena original: {cadena3}")
print(f"Largo de la cadena: {largo_cadena}")

# subcadena [inicio : final ] sin incluir el final  
cadena3 = "hola mundo"

subcadena = cadena3[0:3]
print(f"subcadena de hola: {subcadena}")

subcadena = cadena3[0:4]
print(f"subcadena de hola: {subcadena}")

# replace()

cadena3 = "hola mundo"
print(f"cadena original: {cadena3}")
nueva_cadena = cadena3.replace("mundo", "a todos")
print (nueva_cadena)

#split

datos = "Cristian,100,España"
lista = datos.split(",")
print(lista)

# ===============  cpnversion de datos  ===============
# cadena
numero_cadena = "10"

print(type(numero_cadena))

#entero
numero_entero = int(numero_cadena)

print (type(numero_entero))
print(f"cadena a entero: {numero_entero}")

#float
numero_cadena = "3.1"
numero_float = float(numero_cadena)

print(type(numero_float))
print(f"cadena a float: {numero_float}")

# numero a cadena
numero_entero = 25
cadena4 = str(numero_entero) 

print (type(cadena4))
print(cadena4)

# numero a boolean (0 = false 1 = True)

num = 0
booleano = bool(num)
print(type(booleano))
print(f" numero a cadena {booleano}")

num = 1
booleano = bool(num)
print(type(booleano))
print(f" numero a cadena {booleano}")

num = 5657
booleano = bool(num)
print(type(booleano))
print(f" numero a cadena {booleano}")

#============= operadores logicos =============

# + suma
# - resta / negacion
# * multiplicacion
# ** exponente  2 ** 6 = 64
# / division 
# / / Divion entera 
# % modulo
# and o & (puerta logica and)
# or o | (purta logica or)
# not (puerta logica not)
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que



a = True
b = True
if a & b: 
    print("Los dos son Correcto")
    
a = False
b = True

if a | b: 
    print("Almenos 1 es correcto")