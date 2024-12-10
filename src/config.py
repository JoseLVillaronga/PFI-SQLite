import os
import time
import json
import hashlib
import sqlite3
import getpass
######################
# Conexion SQLite
######################
# Conectar a la base de datos SQLite
# Si el archivo no existe, se creará automáticamente
db_path = 'pfi_database.sqlite'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Crear la tabla de usuarios si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

conn.commit()
###########
# Login
###########
def loguinMain(user, contra):
    # Buscar al usuario en la tabla
    cursor.execute('SELECT * FROM usuarios WHERE nombre = ?', (user,))
    usuario = cursor.fetchone()
    if usuario is not None:
        # Verificar contraseña
        if usuario[1] == user and usuario[2] == hashlib.md5(contra.encode()).hexdigest():
            print("Logueo correcto ...")
            time.sleep(1)
            os.system('clear')
        else:
            os.system('clear')
            print("Logueo incorrecto ...")
            time.sleep(2)
            exit()
    else:
        os.system('clear')
        print("Usuario no encontrado ...")
        time.sleep(2)
        exit()

def filtrar_digitos(cadena):
    """
    Filtra y devuelve solo los caracteres numéricos (0-9) de una cadena dada.
    
    Args:
        cadena (str): La cadena de entrada.

    Returns:
        str: Una nueva cadena que contiene solo los dígitos.
    """
    return ''.join(char for char in cadena if char.isdigit())