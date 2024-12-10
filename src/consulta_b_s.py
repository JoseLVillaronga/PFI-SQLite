import config
config.os.system('clear')
config.cursor.execute('''
    SELECT * FROM productos
    WHERE reposicion >= cantidad
    ''')
res = config.cursor.fetchall()

print('Reporte Stock Bajo ...\n\n')

# Contador
indexx = 0

# Recorre la lista de productos
for doc in res:
    id,nombre,precio,iva,ganancia,cantidad,codigo,reposicion = doc
    # Imprime en pantalla los valores del producto 
    print("--------------------------------------------------------------")
    print("Nombre: ",nombre)
    print("Precio: ",precio)
    print("IVA: ",iva)
    print("Ganancia: ",ganancia)
    # El precio final es el precio al que se le suma el IVA y se multiplica por el factor de ganancia 
    print("Precio final: ",((doc[2] + (doc[2]*doc[3]))*doc[4]))
    print("Cantidad: ",cantidad)
    print("Código: ",codigo)
    print("Cantidad de reposición: ",reposicion)
    print("ID: ",reposicion)

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