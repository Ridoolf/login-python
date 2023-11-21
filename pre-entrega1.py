import json

archive = 'proyecto/db.json'

# TOMA DE DATOS

def get_datos():
    print('-----------------------------------')
    user = input('Ingrese su nombre de usuario: ')
    password = input('Ingrese su contraseña: ')
    return user, password

# VALIDACION DE DATOS

def check_user(user):
    while True:
        if len(user) > 1 and len(user) < 20 and user.isalpha():
            if ' ' not in user:
                return user
        else:
            print('-----------------------------------')
            print('''El usuario no cumple con los requisitos
. Debe tener mas de 1 caracteres
. Debe tener menos de 20 caracteres
. No debe tener espacios
. Deben ser solo letras''')
            print('-----------------------------------')
            user = input('Vuelva a ingresar un usuario valido: ')
    
def check_password(password):
    while True:
        if len(password) >= 5 and len(password) <= 20 and password.isdigit():
            return password
        else:
            print('-----------------------------------')
            print('''La contraseña no cumple con los requisitos
. Debe tener mas de 5 caracteres
. Debe tener menos de 12 caracteres
. Deben ser solo numeros''')
            print('-----------------------------------')
            password = input('Vuelva a ingresar una contraseña valida: ')
            
# LECTURA Y ESCRITURA DE DATOS

def read_archive():
    with open(archive, 'r') as file:
        data = json.load(file)
        return data
    
def write_archive(data, line_indent):
    with open(archive, 'w') as file:
        json.dump(data, file, indent = line_indent)

# REGISTRO, INICIO DE SESION, LECTURA DE BASE DE DATOS Y MENU

def register(user, password):
    try:
        data = read_archive()
    except: 
        data = {'users': []}
        
    for user_in_db in data['users']:
        if user in user_in_db:
            print('-----------------------------------')
            print('El usuario ya existe. Inicie sesion')
            show_menu()
    
    user = check_user(user)        
    password = check_password(password)
            
    new_user = {user : password}    
    data['users'].append(new_user)
    print('-----------------------------------')
    print('Usuario creado con exito')
    
    write_archive(data, 4)
    show_menu()
        
def login(user, password):
    try: 
        data = read_archive()
    except:
        print('-----------------------------------')
        print(f'El usuario {user} no existe en la base de datos')
        show_menu()
        return
        
    for user_in_db in data['users']:
        if user in user_in_db and user_in_db[user] == password:
            print('-----------------------------------')
            print(f'BIENVENIDO: {user.upper()}')
            show_menu()
            return
        
    print('-----------------------------------')
    print('Usuario o contraseña incorrectos. Intente de nuevo')
            
def read_db():
    data = read_archive()
    print('-----------------------------------')
    print(data)
    show_menu()
        
def show_menu():
    print('-----------------------------------')
    res = int(input('''Ingrese la opcion que desea realizar:
1 - Registrarse
2 - Iniciar Sesion
3 - Imprimir datos
0 - Finalizar la ejecucion 
Opcion: '''))
    while res < 0 or res > 3:
        print('-----------------------------------')
        print('Opcion icorrecta.')
        res = int(input('Ingrese la opcion correcta: '))
        
    if res == 1 or res ==  2:
        user, password = get_datos()
        if res == 1:
            register(user, password)
        else:
            login(user, password)
    elif res == 3:
        read_db()
    elif res == 0:
        print('-----------------------------------')
        print('Gracias por utilizar el programa')
        print('-----------------------------------')

# EJECUCION DE FUNCIONES        

show_menu()