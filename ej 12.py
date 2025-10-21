import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps

im = Image.open("mariposa.jpg")
im_gris = ImageOps.grayscale(in)
m = np.array(im_gris)

fil, col = m.shape

for i in range(fil):
    for j in range(col//2):
        aux=m[i][j]
        m[i][j] - ,[i][col-1-j]
        m[i][col-1-j]-aux
    
plt.inshow(m, cmap"gray")
plt.show()