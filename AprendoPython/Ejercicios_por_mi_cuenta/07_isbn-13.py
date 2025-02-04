# comprobacion de isbn-13

isbn = '978-8408285298'

isbn = isbn.replace('-','')
print(isbn)

if len(isbn) != 13:
    print('isbn incorrecto')

isbn_sin_dc =isbn[0:12]
dc_isbn = isbn[-1]

print(isbn_sin_dc)

impar = True
suma = 0

for i in range(len(isbn_sin_dc)):
    num= int(isbn_sin_dc[i])
    if impar:
        suma += num*1
        impar = False
        
    else:
        suma += num*3
        impar=True

print(suma)

dc = 10-(suma%10)

if dc == 10:
    dc = 0

if dc == int(dc_isbn):
    print(f' El isbn: {isbn} es correcto')
else:
    print('El isbn no es correcto')