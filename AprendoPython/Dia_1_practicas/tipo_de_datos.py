cadena = " "
print("esto son 10 espacios :" + (cadena*10) +'fin'  )

palabra = 'python'
print(palabra[1])

palabra = 'python'
print(palabra[0:2])

# listas

numeros = [1,2,3,4,5]
print(numeros)

datos = [1,2,4,"hola"]
print(datos)

print(len(datos))

buscar = (len(datos)-1)
print(buscar)

datos[-2:1]
print(datos)

# juntar listas (se pueden modificar)
print(numeros + datos)

letras = ['a', 'b','c','d']
# coger mas de 1 ele
print(letras[0:3])

a = [1,2,3]
b = [4,6,9]
c = [3,9,1]

r = [a,b,c]

print(r)

# operadores

z = 1+2 == 3
print (z)

zz = 1 >2
print (zz)

l1 = [1,2,3]
l2 = [1,2,3]

listas = len(l1)==len(l2)
print(listas)

c = 'lectura'
d =c[0] == 'H' or c[0] == 'h'
print(d)

a = 5

if a == 2:
    print('a vale 2')
if a == 5:
    print('a vale 5')


n = 7

if n %2 ==0:
    print('es par') 
else:
    print('es impar')


c = 0

while c <= 6:
    print('c vale: ',c)
    c += 1

for i in range(1,11):
    print(f'tabla del (i): {i}',)
    for j  in range(1,11):
        print(f'{i} x {j} = {i * j}')

print()
#opcion = int(input('Dime un numero'))

#for i in range(1,11):
#    print(f'{opcion} x {i} = {i * opcion}')


def sumar(a,b):
    return(a + b)


def es_Par():
    a = int(input('introduce un numero:'))
    if a % 2 == 0:
        return('es par')
    else:
        return('impar')
    

print(es_Par())
