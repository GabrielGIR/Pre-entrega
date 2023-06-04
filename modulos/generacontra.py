import random

def generador_contraseñas():

    print('Genera su contraseña completamente aleatoria!')
    caracters = 'qwertyuiopasdfghjklñzxcvbnm1234567890¿+{},.-<>°|"#$%&/()=??¡¨*[]_:;/*QWERTYUIIOPASDFGHJKLÑZXCVBNM@'
    while True:
        largo= input('La cantidad de caracteres (minimo 8): ')
        largo = int(largo)
        if largo >=8:
            break
        else:
            print('Una cantidad minima de 8 caracteres')

    print('\nSu contraseña: ')

    contraseña =''
    for i in range(largo):
        contraseña += random.choice(caracters)

    return contraseña

print (generador_contraseñas()) 