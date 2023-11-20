# inicio de sesion, registro y lectura de base de datos
import json

archive = 'proyecto/db.json'

def read_archive():
    with open(archive, 'r') as file:
        data = json.load(file)
        return data
    
def write_archive(data, line_indent):
    with open(archive, 'w') as file:
        json.dump(data, file, indent = line_indent)

def register(user, password):
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
    print('Usuario creado con exito')
    
    write_archive(data, 4)
        
def login(user, password):
    data = read_archive()
        
    for user_in_db in data['users']:
        if user in user_in_db and user_in_db[user] == password:
            print(f'BIENVENIDO: {user.upper()}')
            return
        
    print('Usuario o contraseña incorrectos. Intente de nuevo')
    
def read_db():
    data = read_archive()
    print(data)
        
def show_menu():
    res = int(input('''
    Ingrese la opcion que desea realizar:
    1 - Registrarse
    2 - Iniciar Sesion
    3 - Imprimir datos 
    Opcion: '''))
    if res == 1 or res ==  2:
        user = input('Ingrese su nombre de usuario: ')
        password = input('Ingrese su contraseña: ')
        if res == 1:
            register(user, password)
        else:
            login(user, password)
    elif res == 3:
        read_db()
    else:
        print('Opcion icorrecta. Ingrese la opcion correcta')
        
show_menu()
    