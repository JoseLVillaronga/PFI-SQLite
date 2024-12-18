import os
import time

def clear_console():
    if os.name == 'nt':  # 'nt' significa Windows
        os.system('cls')
    else:  # Cualquier otro sistema operativo (Linux, MacOS, etc.)
        os.system('clear')

def mostrar_menu():
   # Lista de opciones 
    options = [
        "\nIngrese la opción del menu correspondiente:\n",
        "1.- Consulta Productos",
        "2.- Alta producto",
        "3.- Suma producto",
        "4.- Resta producto",
        "5.- Baja producto",
        "7.- Busca producto",
        "8.- Reporte Stock Bajo",
        "9.- Cambia cantidad reposición",
        "6.- Salir de la aplicación\n\n"
    ]
   # Imprime lista de opciones 
    for option in options:
        print(option) 

def ejecutar_opcion(opcion):
    if (opcion == '1'):
        # Muestra listado de articulos 
        os.system('python3 src/consulta_test.py')
        clear_console()
    elif (opcion == '2'):
        # Alta de producto 
        os.system('python3 src/consulta_add.py')
        clear_console()
    elif (opcion == '3'):
        # Agrega stock 
        os.system('python3 src/consulta_sum.py')
        clear_console()
    elif (opcion == '4'):
        # Retira stock 
        os.system('python3 src/consulta_res.py')
        clear_console()
    elif (opcion == '5'):
        # Baja de producto 
        os.system('python3 src/consulta_baja.py')
        clear_console()
    elif (opcion == '7'):
        # Baja de producto 
        os.system('python3 src/consulta_busca.py')
        clear_console()
    elif (opcion == '8'):
        # Reporte de stock bajo
        os.system('python3 src/consulta_b_s.py')
        clear_console()
    elif (opcion == '9'):
        # Cambia cantidad de reposición
        os.system('python3 src/cambia_reposicion.py')
        clear_console()
    elif (opcion == '6'):
        # Sale del sistema 
        print("By by ...")
        exit()
    else:
        # Opción no valida 
        print("\n\nOpción no válida. Intente de nuevo.")
        time.sleep(2)
        clear_console()

