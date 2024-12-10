import config
config.os.system('clear')

print("Sumar cantidad en producto\n\n")

codigo1 = str(input("Ingrese código del producto a modificar: "))

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

config.cursor.execute('SELECT * FROM productos WHERE codigo = ?', (codigo1,))
res = config.cursor.fetchone()

print(res)
id,nombre,precio,iva,ganancia,cantidad_anterior,codigo,reposicion = res
print(id,nombre,precio,iva,ganancia,cantidad,codigo,reposicion)
config.time.sleep(8)

if (len(nombre) > 0):
    nueva_cantidad = cantidad + cantidad_anterior
    if (nueva_cantidad > 0):
        try:
            # Actualizar la cantidad para el código especificado
            config.cursor.execute('''
            UPDATE productos
            SET cantidad = ?
            WHERE codigo = ?
            ''', (nueva_cantidad, codigo))
            
            # Confirmar cambios
            config.conn.commit()

            if config.cursor.rowcount > 0:
                print(f"Cantidad actualizada a {nueva_cantidad} para el código '{codigo}'.")
            else:
                print(f"No se encontró un producto con el código '{codigo}'.")
        except config.sqlite3.Error as e:
            print(f"Error al actualizar: {e}")
        finally:
            # Cerrar la conexión
            config.conn.close()
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

