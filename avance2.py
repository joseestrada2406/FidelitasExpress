#Inicio proyecto Fidelitas Express
#Constantes

COSTO_INICIAL = 1000
PESO_MAXIMO = 45
MODULO_EXPRESS = 200
MODULO_BAJO_COSTO = 100
MODULO_INTERNACIONAL = 300
REDUCCION_PESO = 1

#Bienvenida
print("Bienvenido a envíos Fidélitas express")
print("Somos una empresa de hacer envios donde usted los necesite \n")

#Datos de entrada

#Modalidades de envio
print("Se cuenta con 3 modalidades de envío:")
print("Express")
print("Bajo costo")
print("Internacional\n")

#Imprimir costos de los envios
print("Cada paquete tiene un costo inicial de ₡1000 por el primer Kg")
print("Costo por Kilogramo adicional según la modalidad seleccionada: \n")

print("1. Express: ₡200 por kilogramo")
print("2. Bajo costo: ₡100 por kilogramo")
print("3. Internacional: ₡300 por kilogramo\n")

#variable para ejecutar el while
salida = 0
paquetes = 0

while salida < 2:
    if salida <= 1:
#Selección de modalidad y peso de primer paquete
             paquetes = paquetes + 1
             print("Paquete #", paquetes)
             modalidad_seleccionada = int(input("\nSeleccione el número de la modalidad de envío: ")) 

    if modalidad_seleccionada <= 3:
                peso_paquete = float(input("Ingrese el Peso(kg) del paquete: "))

#Calculo del precio a pagar
    if peso_paquete <= float(PESO_MAXIMO):
            salida == 2 
            if modalidad_seleccionada == 1:

                print("\nSe aplicará el cargo de ₡200 por Kg")
                costo_por_kilogramo = COSTO_INICIAL + (MODULO_EXPRESS * (peso_paquete - REDUCCION_PESO))
                print("El costo por el envío del paquete es de:", "₡", costo_por_kilogramo)
                print("\nSu envio fue registrado")
                print("Desea ingresar otro pedido?")
                salida = int(input("1 = Si / 2 = No \n"))
                

            elif modalidad_seleccionada == 2:
                 print("\nSe aplicará el cargo de ₡100 por Kg")
                 costo_por_kilogramo = COSTO_INICIAL + (MODULO_BAJO_COSTO * (peso_paquete - REDUCCION_PESO))
                 print("El costo por el envío del paquete es de:", "₡", costo_por_kilogramo)
                 print("\nSu envio fue registrado")
                 print("Desea ingresar otro pedido?")
                 salida = int(input("1 = Si / 2 = No \n"))

            elif modalidad_seleccionada == 3:
                print("\nSe aplicará el cargo de ₡300 por Kg")
                costo_por_kilogramo = COSTO_INICIAL + (MODULO_INTERNACIONAL * (peso_paquete - REDUCCION_PESO))
                print("El costo por el envío del paquete es de:", "₡", costo_por_kilogramo)
                print("\nSu envio fue registrado")
                print("Desea ingresar otro pedido?")
                salida = int(input("1 = Si / 2 = No \n")) 
    else:            
        print("El peso máximo permitido son 45 kg")

else:
         print("Muchas gracias por realizar el envio con nosotros")
 
#Fin