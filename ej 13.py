import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Crear matriz 4x4 con números del 1 al 16
matriz = np.arange(1, 17).reshape(4, 4)

# Mostrar la matriz
print("Matriz 4x4:")
print(matriz)

# Diagonal principal y contra diagonal
diagonal_principal = [matriz[i][i] for i in range(4)]
contra_diagonal = [matriz[i][3 - i] for i in range(4)]

# Calcular suma y multiplicación
suma_principal = sum(diagonal_principal)
suma_contra = sum(contra_diagonal)

multiplicacion_principal = 1
multiplicacion_contra = 1
for i in range(4):
    multiplicacion_principal *= diagonal_principal[i]
    multiplicacion_contra *= contra_diagonal[i]

# Mostrar resultados
print("\nDiagonal principal:", diagonal_principal)
print("Suma diagonal principal:", suma_principal)
print("Multiplicación diagonal principal:", multiplicacion_principal)

print("\nContra diagonal:", contra_diagonal)
print("Suma contra diagonal:", suma_contra)
print("Multiplicación contra diagonal:", multiplicacion_contra)

# Mostrar la matriz como imagen (solo para verla)
plt.imshow(matriz, cmap='gray')
plt.title("Matriz 4x4")
plt.colorbar()
plt.show()

# la matriz la vemos como imagen por pillow
imagen = Image.fromarray((matriz * 15).astype('uint8')) 
imagen.show()