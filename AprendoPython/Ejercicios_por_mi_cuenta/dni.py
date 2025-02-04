# comprobar dni

dni = '49852630S'
letras = "TRWAGMYFPDXBNJZSQVHLCKE"

if len(dni) != 9 or (dni[-1].isnumeric() == True or dni[0:7].isalpha()== False):
    print('Error: dni Incorrecto')