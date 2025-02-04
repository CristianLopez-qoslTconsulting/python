
#! calcula si este cuadrado es magico

cuadrado_magico = [
    [64,  2,  3, 61, 60,  6,  7, 57],
    [ 9, 55, 54, 12, 13, 51, 50, 16],
    [17, 47, 46, 20, 21, 43, 42, 24],
    [40, 26, 27, 37, 36, 30, 31, 33],
    [32, 34, 35, 29, 28, 38, 39, 25],
    [41, 23, 22, 44, 45, 19, 18, 48],
    [49, 15, 14, 52, 53, 11, 10, 56],
    [ 8, 58, 59,  5,  4, 62, 63,  1]
]
n = len(cuadrado_magico)
es_Magico = True
# numero magico
print("NUMERO MAGICO")

numero_Magico = sum(cuadrado_magico[0])
print(numero_Magico)


# suma Diagonal 1
print("DIAGONAL 1")

suma_diagonal1 = 0

for i in range(n):
    suma_diagonal1+=(cuadrado_magico[i][i])

if suma_diagonal1 != numero_Magico:
    es_Magico = False
print(suma_diagonal1)


# suma Diagonal 2
print("DIAGONAL 2")
suma_diagonal2 = 0
for i in range(n):
    suma_diagonal2 += cuadrado_magico[i][i-1-i]

if suma_diagonal2 != numero_Magico:
    es_Magico = False
print(suma_diagonal2)


# sumaFila
print("SUMA FILA")
for i in range(n):
    if sum(cuadrado_magico[i]) != numero_Magico:
        es_Magico = False
    
print(sum(cuadrado_magico[i]))

# sumaColumna
print("SUMA COLUMNA")
for j in range(n):
    suma_columna = 0
    for i in range(n):
        suma_columna += cuadrado_magico[i][j]
if suma_columna != numero_Magico:
    es_Magico = False
    
print(suma_columna)
# comprobacion
if es_Magico:
    print ("El cuadrado es Magico")
else:
    print("El cuadrado no es Magico")