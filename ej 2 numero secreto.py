import random
num=0
intentos=6
numA=random.randint(1,20)

print("tienes que adivinar un numero secreto")
print()
print("ingrese  un numero")

while(intentos!=0):
    num=int(input())

    if(num==numA):
        print("muy bien! adivinaste el numero")


    else:
        if num<numA:
            print("el numero es mayor")


        else:
            print("el numero es menor")
