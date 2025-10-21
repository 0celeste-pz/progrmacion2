import random
estudiantes= []

estudiantes.append("celeste")
estudiantes.append("angela")
estudiantes.append("berenice")
estudiantes.append("tomas")
estudiantes.append("elvis")
estudiantes.append("morena")
estudiantes.append("theo")

orden=[]

while estudiantes:
    indice=random.randint(0, len(estudiantes)- 1)
    elegido=estudiantes[indice]
    orden.append(elegido)
    estudiantes.pop(indice)


print("el orden de la exposicion es:  ")
for i, nombre in enumerate(orden, start=1):
    print(f"{i}. {nombre}")
