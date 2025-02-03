
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

