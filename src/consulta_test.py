import config
config.os.system('clear')
# Se conecta a la colección productos de la base de datos
collection = config.db['productos']
# Carga la lista completa de productos en "documentos"
documentos = collection.find()

print('Consulta de Productos ...\n\n')

# Contador
indexx = 0

# Recorre la lista de productos
for doc in documentos:
    # Imprime en pantalla los valores del producto 
    print("--------------------------------------------------------------")
    print("Nombre: ",doc["nombre"])
    print("Precio: ",doc["precio"])
    print("IVA: ",doc["iva"])
    print("Ganancia: ",doc["ganancia"])
    # El precio final es el precio al que se le suma el IVA y se multiplica por el factor de ganancia 
    print("Precio final: ",((doc["precio"] + (doc["precio"]*doc["iva"]))*doc["ganancia"]))
    print("Cantidad: ",doc["cantidad"])
    print("Código: ",doc["codigo"])
    print("ID: ",doc["_id"])

    # Paginador: al llegar al 4to valor del contador pausa el bucle for hasta que se preciona una tecla y resetea el contador para volver a mostrar los proximos 4 items de la lista de productos  
    if indexx == 3:
        input("\nPresione Enter para ver nueva página ...")
        indexx = -1
        config.os.system('clear')
        print('Consulta de Productos ...\n\n')
    
    # Abanza el contador 
    indexx += 1

# Al terminar pausa el script hasta que se presiona un tecla
input("\nPresione Enter para volver al menú principal ...")
exit()