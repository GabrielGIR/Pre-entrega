
import os
import json

db = {}
id_clientes = 0

class Usuario:
    def __init__(self, id):
        self.id = id

class Cliente(Usuario):
    def __init__(self, id, nombre):
        super().__init__(id)
        self.nombre = nombre

    def login():
        user = input('Ingrese su usuario: ')
        pwd = input('Ingrese su contraseña: ')
        if len(user) < 4:
            print('Los caracteres mínimos son 4')
        elif len(pwd) < 8:
            print('Cáracteres insuficientes')
        elif user in db and db[user]['pwd'] == pwd:
            print(f'Bienvenido, {user}!')
        else:
            print('Usuario o contraseña incorrectos')

def register():
    global id_clientes
    user = input('Crear nombre de usuario: ')
    pwd = input('Crear contraseña: ')
    pwdC = input('Confirmar contraseña: ')
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

def pagina():
    os.system('cls')
    while True:
        print('\n\nPágina genérica\n')
        accOrLog = input('Iniciar sesión: 1\nRegistrarse: 2\nSalir: 3\nOpción: ')
        if accOrLog == '1':
            Cliente.login()
        elif accOrLog == '2':
            register()
        elif accOrLog == '3':
            print("Chau")
            break
        else:
            print('Por favor ingresa una opción válida')

try:
    with open("usuarios.json", 'r') as file:
        db = json.load(file)
except Exception as e:
    print('Error al leer la base de datos')
    db['usuarios'] = {}

pagina()