# Preguntar el nombre del usuario
nombre = input("¿Cómo te llamas? ")

# Saludar al usuario
print("¡Hola, " + nombre + "!")

# Preguntar el año de nacimiento
año_nacimiento = int(input("¿En qué año naciste? "))

# Calcular la edad (usando el año actual, por ejemplo 2025)
año_actual = 2025
edad = año_actual - año_nacimiento

# Mostrar la edad del usuario
print(nombre + ", tienes aproximadamente " + str(edad) + " años.")
