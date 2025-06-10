def total_factura(importe, iva=21):
    total = importe + (importe * iva / 100)
    return total


print(total_factura(100))       
print(total_factura(100, 10))   
