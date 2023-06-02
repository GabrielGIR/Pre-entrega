import os 
import json

db={}
db['usuarios']={}


def register():
    user= input('Crear nombre de usuario: ')
    pwd= input('Crear Contraseña: ')
    pwdC= input('Confirmar Contraseña: ')
    if len(user) < 4:
        print('Los caracteres minimos son 4')
    elif pwd != pwdC:
        print('Las contraseñas no son iguales')
    elif len(pwd) < 8:
        print('Cáracteres insuficientes')
    elif user in db['usuarios']:
        print('usuario existe')
    else:
        db['usuarios'][user] = pwd
        dbfile = open('usuarios.json', 'w')
        json.dump(db, dbfile)
        print('Usuario creado!')

def login():
    user= input('Ingrese su usuario: ')
    pwd= input('Ingrese su contraseña: ')
    if len(user) < 4 :
        print('Los caracteres minimos son 4')
    elif len(pwd) < 8:
        print('Cáracteres insuficientes')
    elif db['usuarios'][user] == pwd:
        print(f'Bienvenido! {user}')
    else:
        print('No coincide')

def pagina(accOrLog=None):
    os.system('cls')
    while True:
        print('\n\nPágina génerica\n')
        accOrLog= input('Iniciar sesión: 1\nRegistrarse: 2\nSalir: 3\nOpcion: ')
        if accOrLog == '1':
            login()
        elif accOrLog == '2':
            register()
        elif accOrLog == '3':
            print("Chau")
            break
        else:
            print('Porfavor ingresa una de las opciones')

try:
    file = open("usuarios.json", 'r')
    db = json.loads(file.read())
except Exception as e:
    print(f'Error al leer la Base de datos')
    db['usuarios'] = {}

pagina()







def register():
    global id_clientes
    user= input('Crear nombre de usuario: ')
    pwd= input('Crear Contraseña: ')
    pwdC= input('Confirmar Contraseña: ')
    id_cliente += 1
    if len(user) < 4:
        print('Los caracteres minimos son 4')
    elif pwd != pwdC:
        print('Las contraseñas no son iguales')
    elif len(pwd) < 8:
        print('Cáracteres insuficientes')
    elif user in db:
        print('usuario existe')
    else:
        db[user] = pwd
        dbfile = open('usuarios.json', 'w')
        json.dump(db, dbfile)
        print('Usuario creado!')


















class usuario:
    def __init__(self,id):
        self.id = id


class cliente(usuario):
    def __init__(self,id,identidad,residencia,tarjeta,):
        super().__init__(id)
        self.nombre = identidad
        self.residencia = residencia
        self.tarjeta = tarjeta


class proveedor(usuario):
    def __init__(self, id,empresa,local,cuentabancaria):
        super().__init__(id)
        self.empresa = empresa
        self.local = local
        self.cuentabancaria = cuentabancaria

    




    