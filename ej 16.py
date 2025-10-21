from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

imagen = Image.open("imagen.jpg").convert("L")  # profe aca tiene que cambiar segun su archivo
matriz = np.array(imagen)

def rotar_imagen(matriz, opcion):
    if opcion == 1: 
        return np.rot90(matriz)
    elif opcion == 2:  
        return np.rot90(matriz, -1)
    elif opcion == 3: 
        return np.rot90(matriz, 2)
    else:
        print("Opción no válida.")
        return matriz

plt.imshow(matriz, cmap='gray')
plt.title("Imagen original")
plt.axis('off')
plt.show()

print("Opciones de rotación:")
print("1 - 90° a la izquierda")
print("2 - 90° a la derecha")
print("3 - 180°")

opcion = int(input("Elegí una opción (1, 2 o 3): "))

matriz_rotada = rotar_imagen(matriz, opcion)

plt.imshow(matriz_rotada, cmap='gray')
plt.title("Imagen rotada")
plt.axis('off')
plt.show()
