import config
config.os.system('clear')
kelvin_celsius = 273 # Valor utilizado para convertir de Kelvin a Celsius
#puedo definir alguna variable que me ayude a la conversion???

temperatura_c = float(input("Ingrese el valor de temperatura en grados Celsius: "))

temperatura_k = temperatura_c + kelvin_celsius
# Formula de conversion a F = 1.8 * c + 32
temperatura_f = (1.8 * temperatura_c) + 32 #completar formula 

print("El valor de la temperatura expresada en Celsius es: ", temperatura_c)
print("El valor de la temperatura expresada en Kelvin es: ", temperatura_k)
print("El valor de la temperatura expresada en Farenheith es: ", temperatura_f)

input("\nPresione Enter para volver al menú principal ...")
exit()
