#!/usr/bin/env python3
from src import config
from src import funciones
config.os.system('clear')

# Ingreso de usaurio del sistema
user=str(input("Ingresar usuario: "))
# Ingreso de contraseña enmascarada
contra=config.getpass.getpass("Ingresar contraseña: ")

# Ejecuta login con los datos de sesión ingresados antes
config.loguinMain(user,contra)

while True:
    # Muestra opciones del menu 
    funciones.mostrar_menu()

    # Ingreso de opción 
    opcion = input("\nSeleccione una opción: ")
    
    # Ejecuta la opción ingresada anteriormente 
    funciones.ejecutar_opcion(opcion)
