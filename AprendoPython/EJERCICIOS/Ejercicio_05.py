# maquina de chuches sin controlar excepciones

f = open("maquina_de_Golosinas.txt", "r")

# leer indice de las matrices
indice_matriz= int(f.readline())
print (indice_matriz)

# leer la primera matriz chuches(nombre de las chuches)
matriz_chuches = []
for i in range(indice_matriz):
    fila = f.readline().strip().split(",")
    matriz_chuches.append(fila)
    
print(matriz_chuches)

# leer la segunda matriz precios(precio de las chuches)
matriz_precios = []
for i in range(indice_matriz):
    fila2 =list (map( float,f.readline().strip().split(",")))
    matriz_precios.append(fila2)
    
print(matriz_precios)

# leer la tercera matriz_almacen (unidades restantes en la maquina)
matriz_almacen = []

for i in range(indice_matriz):
    fila3 = list(map(int,f.readline().strip().split(",")))
    matriz_almacen.append(fila3)

print(matriz_almacen)

matriz_ventas=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

# fin de lectura de fichero
while True:
    print("============== MAQUINA CHUCHES ==============")
    print("1.- Comprar Chuche")
    print("2.- Mostrar Chuches")
    print("3.- Rellenar Maquina")
    print("4.- Apagar Maquina")
    print("Elige una opcion...")

    opcion = int(input())
    
    if opcion == 1:
        for i in range(len(matriz_chuches)):
            for j in range(len(matriz_chuches[i])):  
                print(f"[Nº {str(i) + str(j):<2}] - {matriz_chuches[i][j]} ({matriz_precios[i][j]:4.2f} $)")
            print()

    coordenada = int(input("Elige una chuche:"))
    num1 = int(coordenada/10) 
    num2 = int(coordenada%10)

    if matriz_almacen[num1][num2] > 0:
        print("Has comprado:",matriz_chuches[num1][num2],matriz_precios[num1][num2],"$")
        matriz_almacen[num1][num2]-=1
        matriz_ventas[num1][num2]+=1
    else:
        print ("No quedan unidades")
        



