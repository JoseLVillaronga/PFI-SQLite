import os
import time

def mostrar_menu():
   # Lista de opciones 
    options = [
        "\nIngrese la opción del menu correspondiente:\n",
        "1.- Consulta Productos",
        "2.- Alta producto",
        "3.- Suma producto",
        "4.- Resta producto",
        "5.- Baja producto",
        "6.- Salir de la aplicación\n\n"
    ]
   # Imprime lista de opciones 
    for option in options:
        print(option) 

def ejecutar_opcion(opcion):
    if (opcion == '1'):
        # Muestra listado de articulos 
        os.system('python3 src/consulta_test.py')
        os.system('clear')
    elif (opcion == '2'):
        # Alta de producto 
        os.system('python3 src/consulta_add.py')
        os.system('clear')
    elif (opcion == '3'):
        # Agrega stock 
        os.system('python3 src/consulta_sum.py')
        os.system('clear')
    elif (opcion == '4'):
        # Retira stock 
        os.system('python3 src/consulta_res.py')
        os.system('clear')
    elif (opcion == '5'):
        # Baja de producto 
        os.system('python3 src/consulta_baja.py')
        os.system('clear')
    elif (opcion == '6'):
        # Sale del sistema 
        print("By by ...")
        exit()
    else:
        # Opción no valida 
        print("\n\nOpción no válida. Intente de nuevo.")
        time.sleep(2)
        os.system('clear')
