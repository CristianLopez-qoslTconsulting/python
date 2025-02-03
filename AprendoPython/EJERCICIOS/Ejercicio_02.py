
#! 03.- Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que
#! sólo es divisible entre él mismo y la unidad.

print("INTRODUCE UN NUMERO")
num = input()
num_entero = int(num)
primo = True

for n in range (2,num_entero,1):
    if (num_entero % n) == 0:
        primo = False
        break

print(num_entero,primo)