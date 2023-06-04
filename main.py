import os
import json
from modulos import generacontra

db = {}
id_clientes = 1 #PARA INCREMENTAR EL ID DE LOS USUARIOS DE FORMA CRECIENTE

class Usuario:
    def __init__(self, id):
        self.id = id

class Cliente(Usuario):
    def __init__(self, id, nombre):
        super().__init__(id)
        self.nombre = nombre

    def login(): #LOGIN ES EL MISMO QUE LA PRE-ENTREGA 1 PERO EL REGISTER FUE ACTUALIZADO
        user = input('Ingrese su usuario: ')
        pwd = input('Ingrese su contraseña: ')
        if len(user) < 4:
            print('Los caracteres mínimos son 4')
        elif len(pwd) < 8:
            print('Cáracteres insuficientes')
        elif user in db and db[user]['pwd'] == pwd:
            print(f'Bienvenido, {user}!')
            carrito_compras(user)
        else:
            print('Usuario o contraseña incorrectos')

def register():
    global id_clientes #EL GLOBAL PARA DECIR QUE EL ID_CLIENTES ES UNA VARIABLE GLOBAL 
    user = input('Crear nombre de usuario: ')
    choice = input('¿Desea generar una contraseña aleatoria? (s/n): ')

    if choice.lower() == 's':
        pwd = generacontra.generador_contraseñas()
        print(f'Su contraseña generada aleatoriamente es: {pwd}')
    else:
        pwd = input('Crear contraseña: ')

    pwdC = input('Confirmar contraseña(En caso de haber generado una, copiar contraseña y pegarla): ') #PARA COPIAR Y PEGAR LA CONTRASEÑA COPIARLA CON CTRL+V Y PEGARLA CON EL CLICK DERECHO
    id_clientes += 1
    if len(user) < 4:
        print('Los caracteres mínimos son 4')
    elif pwd != pwdC:
        print('Las contraseñas no coinciden')
    elif user in db:
        print('El usuario ya existe')
    else:
        db[user] = {
            'pwd': pwd,
            'id': id_clientes
        }
        with open('usuarios.json', 'w') as dbfile:
            json.dump(db, dbfile)
        print('Usuario creado!')


def carrito_compras(user): 
    carrito = []
    while True:
        os.system('cls')
        print(f'\n\nCarrito de Compras - Usuario: {user}\n')
        print('1. Agregar producto al carrito')
        print('2. Ver carrito')
        print('3. Finalizar compra')
        print('4. Volver')
        opcion = input('Opción: ')
        
        if opcion == '1':
            producto = input('Ingrese el nombre del producto: ')
            carrito.append(producto)
            print(f'Producto "{producto}" agregado al carrito.')
            input('Presione Enter para continuar...')
        elif opcion == '2':
            if carrito:
                print('Productos en el carrito:')
                for producto in carrito:
                    print(f'- {producto}')
            else:
                print('El carrito está vacío.')
            input('Presione Enter para continuar...')
        elif opcion == '3':
            if carrito:
                print('Compra finalizada. ¡Gracias por su compra!')
                carrito.clear()
                input('Presione Enter para continuar...')
            else:
                print('El carrito está vacío.')
                input('Presione Enter para continuar...')
        elif opcion == '4':
            break
        else:
            print('Por favor, ingrese una opción válida.')
            input('Presione Enter para continuar...')

def pagina():
    while True:
        os.system('cls')
        print('\n\nPágina genérica\n')
        print('1. Iniciar sesión')
        print('2. Registrarse')
        print('3. Salir')
        opcion = input('Opción: ')

        if opcion == '1':
            Cliente.login()
        elif opcion == '2':
            register()
        elif opcion == '3':
            print("Chau")
            break
        else:
            print('Por favor, ingrese una opción válida.')
            input('Presione Enter para continuar...')



try:
    with open("usuarios.json", 'r') as file:
        db = json.load(file)
except Exception as e:
    print('Error al leer la base de datos')
    db['usuarios'] = {}

pagina()
    




    