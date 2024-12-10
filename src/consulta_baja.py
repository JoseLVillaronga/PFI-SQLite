import config
config.os.system('clear')

print("Baja de producto\n\n")

codigo1 = str(input("Ingrese código del producto eliminar: "))

config.cursor.execute('SELECT * FROM productos WHERE codigo = ?', (codigo1,))
res = config.cursor.fetchone()

id,nombre,precio,iva,ganancia,cantidad_anterior,codigo,reposicion = res


if (len(nombre) > 0):
    try:
        # Borrar el registro con el código especificado
        config.cursor.execute('''
        DELETE FROM productos
        WHERE codigo = ?
        ''', (codigo,))
        
        # Confirmar cambios
        config.conn.commit()

        if config.cursor.rowcount > 0:
            print(f"Producto con código '{codigo}' eliminado exitosamente.")
            config.time.sleep(3)
        else:
            print(f"No se encontró un producto con el código '{codigo}'.")
    except config.sqlite3.Error as e:
        print(f"Error al eliminar: {e}")
        config.time.sleep(3)
    finally:
        # Cerrar la conexión
        config.conn.close()
else:
    print("El producto ingresado no existe ...")
    config.time.sleep(3)
    exit()