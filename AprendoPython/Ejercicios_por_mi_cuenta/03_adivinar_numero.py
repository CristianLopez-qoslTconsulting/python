
#adivinar un numero en 5 intentos (el numero sera entre 1 y 50)

import random


intentos = True

num_random = random.randint(1,50)

while intentos:
    opcion = int(input('Introduce un numero ente 1 y 50: '))
    if opcion == num_random:
        print(f'Has acetado el numero era {num_random}')
        intentos = False

    elif opcion > num_random:
        print(f'El numero {opcion} es mayor')
    
    elif opcion < num_random:
        print(f'El numero {opcion} es menor')
    

    