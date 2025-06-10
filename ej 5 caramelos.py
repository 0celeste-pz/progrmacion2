c=0
e=0
ce=0
cs=0

print("¿cuantos caramelos tiene que entregar?")
c=int(input())

print("¿cuantos estudiantes son?")
e=int(input())

ce=c//e
cs=c-(ce*e)

print("a cada estudiante se les entrega ",ce)
print("y sobran ",cs)
