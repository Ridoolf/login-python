# inicio de sesion, registro y lectura de base de datos
import json

archive = 'proyecto/db.json'

def register():
    user = input('Ingrese su nombre de usuario: ')
    password = input('Ingrese su contraseña: ')
    
    try:
        with open(archive, 'r') as file_in_db:
            data = json.load(file_in_db)
    except: 
        data = {'users': []}
        
    for user_in_db in data['users']:
        if user in user_in_db:
            print('El usuario ya existe. Inicie sesion')
            return
    
    new_user = {user : password}    
    data['users'].append(new_user)
    
    with open(archive, 'w') as file:
        json.dump(data, file, indent = 4)
        
def login():
    user = input('usuario: ')
    password = input('contraseña: ')
    
    with open(archive, 'r') as file:
        data = json.load(file)
        
    for user_in_db in data['users']:
        if user in user_in_db and user_in_db[user] == password:
            print(f'BIENVENIDO: {user.upper()}')
            return
        
    print('Usuario o contraseña incorrectos. Intente de nuevo')
    
def read_db():
    with open(archive, 'r') as file:
        data = json.load(file)
        print(data)
        
def show_menu():
    res = int(input('''
                Ingrese la opcion que desea realizar:
                1 - Iniciar Sesion
                2 - Registrarse
                3 - Imprimir datos 
                '''))
    if res == 1:
        login()
    elif res == 2:
        register()
    elif res == 3:
        read_db()
    else:
        print('Opcion icorrecta. Ingrese la opcion correcta')
        
show_menu()
    