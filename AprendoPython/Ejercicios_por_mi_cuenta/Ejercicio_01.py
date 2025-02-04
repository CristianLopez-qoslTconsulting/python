''' 01.- Escribe un programa que muestre los n primeros términos de la serie de Fibonacci. El primer término de la serie de
Fibonacci es 0, el segundo es 1 y el resto se calcula sumando los dos anteriores, por lo que tendríamos que los términos
son 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144... El número n se debe introducir por teclado.'''

digito1 = 0
digito2 = 1
fibonaci = 0

for i in range (0,21,1):
    digito1 = digito2
    digito2 = fibonaci
    print(fibonaci)
    fibonaci = digito1 + digito2
    