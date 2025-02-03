#00-Escribe un programa que diga cuál es la última cifra de un número entero introducido por teclado.

print("Dime un numero")
num = input()
numero_entero = int(num)
print(type (numero_entero))

ultima_cifra = numero_entero % 10
print("Ultima cifra:",ultima_cifra)