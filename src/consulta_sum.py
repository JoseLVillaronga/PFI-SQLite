import config
config.os.system('clear')

collection = config.db['productos']

print("Sumar cantidad en producto\n\n")

codigo = str(input("Ingrese código del producto a modificar: "))

filtro = {"codigo": codigo}

cantidad = int(input("Cantidad a sumar: "))

i = 0

while cantidad < 1:
    if (i > 2):
        print("Supero a cantidad de intentos ...")
        config.time.sleep(2)
        exit()
    else:
        print("La cantidad la sumar debe ser mayor a '0'")
        config.time.sleep(2)
        i += 1

producto = collection.find_one({"codigo": codigo})

if (producto is not None):
    cantidad_anterior=producto["cantidad"]
    cantidad = cantidad + cantidad_anterior
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
    print("El producto no existe")
    config.time.sleep(2)
    exit()

