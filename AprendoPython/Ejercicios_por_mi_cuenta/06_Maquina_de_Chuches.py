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
print('''

''')
# fin de lectura de fichero
suma_precio = 0
while True:
    print("============== MAQUINA CHUCHES ==============")
    print("1.- Comprar Chuche")
    print("2.- Mostrar Chuches")
    print("3.- Rellenar Maquina")
    print("4.- Apagar Maquina")
    print("Elige una opcion...")
    
    
    opcion = int(input())
    if opcion > 4:
        print('Elige una opcion corresta')

    # punto 1
    if opcion == 1:
        for i in range(len(matriz_chuches)):
            for j in range(len(matriz_chuches[i])):  
                print(f"[Nº {str(i) + str(j):<2}] - {matriz_chuches[i][j]} ({matriz_precios[i][j]:4.2f} $)")
        print()

        coordenada = int(input("Elige una chuche:"))  
        num1 = int(coordenada/10) 
        num2 = int(coordenada%10)

        if matriz_almacen[num1][num2] > 0:
            print("Has comprado:", matriz_chuches[num1][num2], matriz_precios[num1][num2], "$")
            matriz_almacen[num1][num2] -= 1
            matriz_ventas[num1][num2] += 1
            suma_precio +=float(matriz_precios[num1][num2]) 
        else:
            print("No quedan unidades")
    
    #punto 2
    if opcion == 2:
        print("---------------------------------------------")
        for i in range(len(matriz_chuches)):
            for j in range(len(matriz_chuches[i])):  
                if matriz_almacen[i][j] >=1:
                    print(f"[Nº {str(i) + str(j):<2}] - {matriz_chuches[i][j]} ({matriz_precios[i][j]:4.2f} $) (Cantidad: {matriz_almacen[i][j]})")
            print()
        print("---------------------------------------------")

    #punto 3
    if opcion == 3:
        print("---------------------------------------------")
        contraseña = "maquina17"

        supuesta_contraseña = str(input("Introduce contraseña: "))

        if contraseña != supuesta_contraseña:
            print("contraseña incorrecta")

        else:
            print("contraseña correcta")
            chuche_rellenar = int(input("Dime la chuche que quieres rellenar: "))
            digito1 = chuche_rellenar/10
            digito2 = chuche_rellenar%10

            cantidad_Rellenar = int(input("Dime la cantidad que quieres introducir: "))
            matriz_almacen[digito1][digito2] += cantidad_Rellenar

            print(matriz_almacen)

    if opcion == 4:
       print("---------------------------------------------")
     
       for i in range(len(matriz_chuches)):
            for j in range(len(matriz_chuches[i])):
                if matriz_ventas[i][j] > 0:
                    print("Han comprado: ",matriz_chuches[i][j],"  ",matriz_ventas[i][j],"  ", matriz_precios[i][j],"$")
       print("------------------------ GANANCIAS ------------------------")
       print("La maquina a generado: ",suma_precio,"$")
       print("-----------------------------------------------------------")
       break