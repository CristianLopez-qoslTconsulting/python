# comprobar dni
def comprueba_dni():
    dni = input('Dime tu dni: ')
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    if len(dni) != 9 or dni[-1].isdigit()  or not dni[0:8].isdigit():
        print('Error: dni Incorrecto')

    dni_sin_letra = int(dni[0:8])
    letra_dni = dni[-1]

    supuesta_Letra = letras[dni_sin_letra%23]

    if letra_dni == supuesta_Letra:
        return(f'El dni [{dni}] es correcto')
    else:
        return(f'El dni [{dni}] no es correcto')

print(comprueba_dni())