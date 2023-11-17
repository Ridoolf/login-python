# inicio de sesion, registro y lectura de base de datos
import json

archive = 'proyecto/db.txt'

def register():
    user = input('Ingrese su nombre de usuario: ')
    password = input('Ingrese su contraseña: ')
    
    new_data = {
        user : password
    }
    
    with open(archive, 'r') as file_in_db:
        for line in file_in_db:
            data = json.loads(line)
            if user in data:
                print('El usuario ya existe. Inicie sesion')
                return
    file_in_db.close()
    
    with open(archive, 'a') as file:
        json.dump(new_data, file)
        file.write('\n')
    
def login():
    user = input('usuario: ')
    password = input('contraseña: ')
    
    with open(archive, 'r') as file:
        for line in file:
            data = json.loads(line)
            if user in data and data[user] == password:
                print(f'Bienvenido {user}') 
                return True
        
    print('Usuario o contraseña incorrectos. Intente de nuevo')

def read_db():
    with open(archive, 'r') as file:
        for line in file:
            data = json.loads(line)
            for userName, password in data.items():
                print(f'Usuario: {userName}')
                print(f'Contraseña: {password}')
                print('-------')
            
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
    