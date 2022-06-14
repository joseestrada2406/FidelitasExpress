#Inicio

print("Envíos Fidélitas express")
print()

#Datos de entrada

#Modalidades de envio
print("Se cuenta con 3 modalidades de envío:")
print("Express")
print("Bajo costo")
print("Internacional")
print()

#Costos
print("Cada paquete tiene un costo inicial de ₡1000 por el primer Kg")
print("Costo por Kilogramo adicional según la modalidad seleccionada:")
Express = print("Express: ₡200 por kilogramo")
Bajo_costo = print("Bajo costo: ₡100 por kilogramo")
Internacional = print("Internacional: ₡300 por kilogramo")
print("El peso maximo permitido es de 45 kg")
print()

#Selección de modalidad y peso de primer paquete
paquete_1 = print("Paquete #1")
Modalidad_seleccionada = input("Modalidad de envío:")
peso = float(input("Peso(kg):"))

#Calculo del precio a pagar

if Modalidad_seleccionada == "Express":
    print("Se aplicará el cargo de ₡200 por Kg")
    Costo_por_kilogramo = (peso * 1000) + (200 * peso)
elif Modalidad_seleccionada == "Bajo costo":
    print("Se aplicará el cargo de ₡100 por Kg")
    Costo_por_kilogramo = (peso * 1000) + (100 * peso)
else:
    Modalidad_seleccionada == "Internacional"
    print("Se aplicará el cargo de ₡300 por Kg")
    Costo_por_kilogramo = (peso * 1000) + (300 * peso)

#Resultados

print("El costo por el envio del paquete #1 es de:", "₡", Costo_por_kilogramo)

#Fin

