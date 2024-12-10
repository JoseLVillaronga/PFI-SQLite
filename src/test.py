import config

# Conexion a la base de datos SQLite
db_path = 'pfi_database.sqlite'
conn = config.sqlite3.connect(db_path)
cursor = conn.cursor()

# IDs y el nuevo valor para reposicion
ids_actualizar = (13, 14)  # Tupla con los IDs que deseas actualizar
nuevo_valor_reposicion = 50

try:
    # Actualizar el campo reposicion donde el id está en la lista de valores
    cursor.execute(f'''
    UPDATE productos
    SET reposicion = ?
    WHERE id IN ({','.join(['?'] * len(ids_actualizar))})
    ''', (nuevo_valor_reposicion, *ids_actualizar))
    
    # Confirmar cambios
    conn.commit()

    print(f"El campo 'reposicion' se actualiza a {nuevo_valor_reposicion} para los IDs {ids_actualizar}.")
except config.sqlite3.Error as e:
    print(f"Error al actualizar: {e}")
finally:
    # Cerrar la conexi�n
    conn.close()

config.time.sleep(7)