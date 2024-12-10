import config
config.os.system('clear')
# Se conecta a la colección productos de la base de datos
#collection = config.db['productos']
# Carga la lista completa de productos en "documentos"
#documentos = collection.find()
config.cursor.execute('SELECT * FROM productos')
res = config.cursor.fetchall()

print('Consulta de Productos ...\n\n')

# Contador
indexx = 0

# Recorre la lista de productos
for doc in res:
    # Imprime en pantalla los valores del producto 
    print("--------------------------------------------------------------")
    print("Nombre: ",doc[1])
    print("Precio: ",doc[2])
    print("IVA: ",doc[3])
    print("Ganancia: ",doc[4])
    # El precio final es el precio al que se le suma el IVA y se multiplica por el factor de ganancia 
    print("Precio final: ",((doc[2] + (doc[2]*doc[3]))*doc[4]))
    print("Cantidad: ",doc[5])
    print("Código: ",doc[6])
    print("ID: ",doc[0])

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