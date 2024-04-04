mi_diccionario = {}
import os 
sw = True 

def fnt_agregar( diccionario, Nombre, Apellido, Contacto, correo, edad, estrato, sexo ,direccion ):
    if Nombre == " " or Apellido == " " or Contacto == " " or correo == " " or edad == " " or estrato == " " or sexo == " " or direccion == " ":
        enter = input("Ingrese toda la informacion solicitada")
    else:
        diccionario[Nombre] = {"Nombre": Nombre, "apellido": Apellido, "Contacto": Contacto, "Correo": correo, "Estrato": estrato, "Sexo": sexo, "Direccion": direccion }
        enter = input(f'\nLa persona {Nombre} ha sido registrada con éxito <ENTER>')
        
def fnt_selector (op):
    if op == '1':
        os.system('cls')
        nombre = input('Nombre:  ')
        Apellido = input('Apellido: ')
        correo = input('Correo:  ')
        Contacto = input('Contacto: ')
        direccion=input('Dirección: ')
        edad = input('Edad:   ')
        estrato = input('Estrato: ')
        sexo = input('Sexo [M/F]: ')
        fnt_agregar(mi_diccionario,nombre,Apellido,Contacto,correo,edad,sexo,direccion,estrato)

while sw == True:
       os.system('cls')
        opcion = input('1. Registrar\n2. Mostrar\n3. Salir\n- >  ')
    if opcion == '1':
        fnt_selector(opcion)
    elif opcion == '2':
        os.system('cls')
        print('\nCantidad de registros: ',len(mi_diccionario),'\n')
        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")
        enter = input('\n\nPresione ENTER para continuar...')
    elif opcion == '3':
        sw = False


