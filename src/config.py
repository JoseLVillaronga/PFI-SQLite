import os
import time
import json
import hashlib
import getpass
######################
# Conexion MongoDB
######################
from pymongo import MongoClient
# Define las credenciales de acceso a la base de datos
usuario = 'pfi'
password = 'pfi123'
# Define la URL de conexión 
client = MongoClient(f'mongodb://{usuario}:{password}@localhost:27017/')
# Seleccionar la base de datos
db = client['PFI']
###########
# Login
###########
def loguinMain(user,contra):
    collection = db['usuarios']
    usuario = collection.find_one({"nombre": user})
    if (usuario is not None):
        # La condición 'usuario is not nome' indica que el usuario fue encontrado en la base de datos 
        if (usuario["nombre"] == user):
            if ((usuario["password"] == hashlib.md5(contra.encode()).hexdigest())):
                # Compara que el hash MD5 de la contraseña ingresada en la función coninsida con el hash MD5 guardado en la base de datos para este usuario y si es así ejecuta lo que sigue a continuación
                print("Logueo correcto ...")
                time.sleep(1)
                os.system('clear')
            else:
                # Si el hash MD5 de la contraseña ingresada en la función no coninside con el hash MD5 guardado en la base de datos para este usuario ejecuta lo que sigue a continuación
                os.system('clear')
                print("Logueo incorrecto ...")
                time.sleep(2)
                exit()
        else:
            os.system('clear')
            print("Logueo incorrecto ...")
            time.sleep(2)
            exit()
    else:
        # Si el usuario endresado en la función no es encontrado en la base de datos ejecuta lo siguiente ...
        os.system('clear')
        print("Usuario no encontrado ...")
        time.sleep(2)
        exit()