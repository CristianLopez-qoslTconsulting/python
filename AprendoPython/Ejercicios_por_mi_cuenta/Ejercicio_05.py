
import time

calculadora_on = True

while calculadora_on:

      print(''' **********  calculadora  **********
            
            1.- Suma
            2.- Multipliar
            3.- Restar
            4.- Dividir
            5.- Apagar
             ''')

      opcion = int(input('Elige una opcion: '))

      if opcion > 5:
            print('Introduce una opcion corresta')
      
      elif opcion == 1:
            print('=====  suma =====')
            print('Dime 2 numeros que quieras sumar')
            num_suma_1 = int(input('Numero 1 :'))
            num_suma_2 = int(input('Numero 2 :'))

            suma = num_suma_1 + num_suma_2

            print('El resultado de la suma de ', num_suma_1 ,' + ' , num_suma_2, 'es: ', suma,'\n')
            
      
      elif opcion == 2:
            print(' =====  Multiplica ===== ')
            print('Dime 2 numeros que quieras Multiplicar')
            num_mult_1 = int(input('Numero 1 :'))
            num_mult_2 = int(input('Numero 2 :'))

            mult = num_mult_1 * num_mult_2

            print('El resultado de la multiplicacion es de ', num_mult_1 ,' + ' , num_mult_2, 'es: ', mult,'\n')
      
      elif opcion == 3:
            print(' =====  Restar ===== ')
            print('Dime 2 numeros que quieras Restar')
            num_resta_1 = int(input('Numero 1 :'))
            num_resta_2 = int(input('Numero 2 :'))

            resta = num_resta_1 - num_resta_2

            print('El resultado de la resta es de ', num_resta_1 ,' + ' , num_resta_2, 'es: ',resta,'\n')

      elif opcion == 4:
            print(' =====  Dividir ===== ')
            print('Dime 2 numeros que quieras dividir')
            num_div_1 = int(input('Numero 1 :'))
            num_div_2 = int(input('Numero 2 :'))

            div = num_div_1 - num_div_2

            print('El resultado de la division es de ', num_div_1 ,' + ' , num_div_2, 'es: ',div,'\n')
      
      elif opcion == 5:
            print('Apagando la calculadora...')
            time.sleep(5)
            print('🐍 Calculadora  apagada 🐍')
            
            calculadora_on = False
