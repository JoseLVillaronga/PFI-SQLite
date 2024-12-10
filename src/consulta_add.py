import config
config.os.system('clear')

collection = config.db['productos']

print("Ingresa Producto\n\n")
nombre = str(input("Producto (nombre): "))
precio = float(input("Precio: "))
iva = float(input("IVA: "))
ganancia = float(input("Ganancia: "))
cantidad = int(input("Cantidad: "))
codigo = str(input("Código: "))

res = collection.find_one({"nombre": nombre})

if (res is None):
    documento = {
        "nombre": nombre,
        "precio": precio,
        "iva": iva,
        "ganancia": ganancia,
        "cantidad": cantidad,
        "codigo": codigo
    }
    resultado = collection.insert_one(documento)
    print("ID del producto agregado: ",resultado.inserted_id)
    input("\nPresione Enter para volver al menú principal ...")
    exit()
else:
    print("El producto ya existe ...")
    config.time.sleep(2)
    exit()
