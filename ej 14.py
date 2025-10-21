from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 1 busca a imagen en mis archivos y la convierte en una imagen de colores grises
imagen = Image.open("descarga.jpg")

matriz = np.array(imagen)

plt.imshow(matriz, cmap='gray')
plt.title("descarga.jpg")
plt.axis('off')
plt.show()

matriz_volteada = matriz[:, ::-1]  

plt.imshow(matriz_volteada, cmap='gray')
plt.title(" descarga volteada horizontalmente")
plt.axis('off')
plt.show()