import config
config.os.system('clear')

collection = config.db['productos']

print("Sumar cantidad en producto\n\n")

codigo = str(input("Ingrese código del producto a modificar: "))

filtro = {"codigo": codigo}

cantidad = int(input("Cantidad a restar: "))
producto = collection.find_one({"codigo": codigo})

i = 0

while cantidad < 1:
    if (i > 2):
        print("Supero la cantidad de intentos ...")
        config.time.sleep(2)
        exit()
    else:
        print("La cantidad a sumar debe ser mayor a '0'")
        config.time.sleep(2)
        i += 1

ref = producto["cantidad"] - cantidad 

if ((producto is not None) and ref >= 0):
    cantidad_anterior=producto["cantidad"]
    cantidad = cantidad_anterior - cantidad
    nueva_cantidad = {"$set": {"cantidad": cantidad}} 
    res = collection.update_one(filtro, nueva_cantidad)
    if (res.modified_count > 0):
        print("Producto actualizado con exito ...")
        config.time.sleep(2)
        exit()
    else:
        print("No se actualizo el producto ...")
        config.time.sleep(2)
        exit()
else:
    print("El producto no existe o el resultado es menor a '0'")
    config.time.sleep(2)
    exit()