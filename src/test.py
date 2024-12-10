import config
config.cursor.execute('SELECT * FROM productos')
res = config.cursor.fetchall()

print(res)

config.time.sleep(7)