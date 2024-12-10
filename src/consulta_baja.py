import config
config.os.system('clear')

collection = config.db['productos']

print("Baja de producto\n\n")

codigo = str(input("Ingrese código del producto eliminar: "))

producto = collection.find_one({"codigo": codigo})

if (producto is not None):
    filtro = {"codigo": codigo}
    res = collection.delete_one(filtro)
    if (res.deleted_count > 0):
        print("Producto elimitado exitosamente ...")
        config.time.sleep(2)
        exit()
    else:
        print("El Producto no se pudo eliminar ...")
        config.time.sleep(2)
        exit()
else:
    print("El producto ingresado no existe ...")
    config.time.sleep(2)
    exit()