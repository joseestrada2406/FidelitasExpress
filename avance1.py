#Inicio proyecto Fidelitas Express

COSTO_INICIAL = 1000
PESO_MAXIMO = 45
MODULO_EXPRESS = 200
MODULO_BAJO_COSTO = 100
MODULO_INTERNACIONAL = 300

print("Envíos Fidélitas express")
print()

#Datos de entrada

#Modalidades de envio
print("Se cuenta con 3 modalidades de envío:")
print("Express")
print("Bajo costo")
print("Internacional")
print()

#Imprimir información general en pantalla
print("Cada paquete tiene un costo inicial de ₡1000 por el primer Kg")
print("Costo por Kilogramo adicional según la modalidad seleccionada:")
print("")
print("1. Express: ₡200 por kilogramo")
print("2. Bajo costo: ₡100 por kilogramo")
print("3. Internacional: ₡300 por kilogramo")
print()

#Selección de modalidad y peso de primer paquete
print("Paquete #1")
modalidad_seleccionada = int(input("Seleccione el número de la modalidad de envío: "))
peso_paquete = float(input("Ingrese el Peso(kg) del paquete: "))

#Calculo del precio a pagar
if peso_paquete <= float(PESO_MAXIMO): 
    if modalidad_seleccionada == 1:
        print("Se aplicará el cargo de ₡200 por Kg")
        costo_por_kilogramo = COSTO_INICIAL + (MODULO_EXPRESS * peso_paquete)
        print("El costo por el envío del paquete es de:", "₡", costo_por_kilogramo)
    elif modalidad_seleccionada == 2:
        print("Se aplicará el cargo de ₡100 por Kg")
        costo_por_kilogramo = COSTO_INICIAL + (MODULO_BAJO_COSTO * peso_paquete)
        print("El costo por el envío del paquete es de:", "₡", costo_por_kilogramo)
    elif modalidad_seleccionada == 3:
        print("Se aplicará el cargo de ₡300 por Kg")
        costo_por_kilogramo = COSTO_INICIAL + (MODULO_INTERNACIONAL * peso_paquete)
        print("El costo por el envío del paquete es de:", "₡", costo_por_kilogramo)
    else:
        print("Opción ingresada es inválida")
    
else:
    print("El peso máximo permitido son 45 kg")




#Fin

