import math

# Función para calcular el área de un círculo
def area_circulo(radio):
    return math.pi * radio ** 2

# Función para calcular el volumen
def volumen_cilindro(radio, altura):
    base=area_circulo(radio)
    return base*altura

radio = float(input("el radio del cilindro: "))
altura = float(input("la altura del cilindro: "))

print("El volumen del cilindro es:",volumen_cilindro(radio,altura))
print("el area del circulo es:",area_circulo(radio))
