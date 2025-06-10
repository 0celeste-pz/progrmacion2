from datetime import datetime

def calcular_edad(fecha_nac):
    hoy = datetime.today()
    edad_dias = (hoy - fecha_nac).days

    # Calcular años, meses, días
    años = hoy.year - fecha_nac.year
    meses = hoy.month - fecha_nac.month
    dias = hoy.day - fecha_nac.day

    if dias < 0:
        meses -= 1
        dias += (datetime(hoy.year, hoy.month, 1) - datetime(hoy.year, hoy.month - 1, 1)).days

    if meses < 0:
        años -= 1
        meses += 12

    return edad_dias, años, meses, dias

# Pedir fecha al usuario
fecha_input = input("Ingresa tu fecha de nacimiento (dd/mm/aaaa): ")

fecha_nac = datetime.strptime(fecha_input, "%d/%m/%Y")

# Calcular edad
dias_totales, años, meses, dias = calcular_edad(fecha_nac)

# Mostrar resultados
print("\nEdad total en días:", dias_totales)
print(f"Edad: {años} años, {meses} meses y {dias} días")


