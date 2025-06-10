# Pedir al usuario la cantidad a extraer
cantidad=int(input("Ingrese la cantidad a extraer: "))

b_1000=cantidad//1000
resto=cantidad%1000

b_200=resto//200
resto=resto%200

print("Billetes de 1000:", b_1000)
print("Billetes de 200:", b_200)
print("dinero no diponible:", resto)
