from PIL import Image

# cambai la imagen a gris
def convertir_a_gris(imagen):
    ancho, alto = imagen.size
    
    imagen_gris = Image.new("L", (ancho, alto))

    pixeles = imagen.load()
    pixeles_gris = imagen_gris.load()
    
    for x in range(ancho):
        for y in range(alto):
            r, g, b = pixeles[x, y][:3]  
            gris = int(r*0.2989 + g*0.5870 + b*0.1140)
            pixeles_gris[x, y] = gris
    
    return imagen_gris

imagen_color = Image.open("descarga.jpg")  
imagen_color.show(title="Imagen Original")

imagen_gris = convertir_a_gris(imagen_color)
imagen_gris.show(title="Imagen en Escala de Grises")
