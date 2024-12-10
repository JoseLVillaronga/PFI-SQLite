import config
config.os.system('clear')

# Crear la tabla de productos si no existe
config.cursor.execute('''
CREATE TABLE IF NOT EXISTS productos_new (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE,
        precio REAL NOT NULL,
        iva REAL NOT NULL,
        ganancia REAL NOT NULL,
        cantidad INTEGER NOT NULL,
        codigo TEXT NOT NULL UNIQUE,
        reposicion INTEGER DEFAULT 0
)
''')
config.conn.commit()

print("Ingresa Producto\n\n")
nombre = str(input("Producto (nombre): "))
precio = float(input("Precio: "))
iva = float(input("IVA: "))
ganancia = float(input("Ganancia: "))
cantidad = int(input("Cantidad: "))
codigo = str(input("Código: "))
reposicion = input("Cantidad de Reposición: ")
if len(reposicion) == 0:
    reposicion = 0
else:
    reposicion = config.filtrar_digitos(reposicion)
    reposicion = int(reposicion)

# Verificar si el producto ya existe
config.cursor.execute('SELECT * FROM productos WHERE nombre = ?', (nombre,))
res = config.cursor.fetchone()

if res is None:
    # Insertar nuevo producto
    config.cursor.execute('''
    INSERT INTO productos (nombre, precio, iva, ganancia, cantidad, codigo, reposicion)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nombre, precio, iva, ganancia, cantidad, codigo, reposicion))
    config.conn.commit()
    print("Producto agregado exitosamente.")
    input("\nPresione Enter para volver al menú principal ...")
else:
    print("El producto ya existe ...")
    config.time.sleep(2)
    exit()