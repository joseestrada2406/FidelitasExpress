import io 


COSTO_INICIAL = 1000
PESO_MAXIMO = 45
MODULO_EXPRESS = 200
MODULO_BAJO_COSTO = 100
MODULO_INTERNACIONAL = 300
REDUCCION_PESO = 1
listaPedidos = [[1, 'Jose Estrada', 402310691, 'Experian', 'Express', 2800.0, 10.0]]
identificador_paquete = 0
if (len(listaPedidos) > 0 ):
    identificador_paquete = int(listaPedidos[-1][0])


def flujoPrincipalProyecto():
    SALIDA = 0
    seleccionModulo = 0
    seleccionSeguir = 0

    bienvenida()
    while SALIDA == 0:
        menuModulos()
        seleccionModulo = int(input("Seleccione el módulo al que desea acceder: "))
        if seleccionModulo == 1:
            moduloEnvio()
        elif seleccionModulo == 2:
            moduloFacturacion()
            #seleccionSeguir = int(input("Desea realizar otra operación: 1=Si / 2=No "))
            #if seleccionSeguir == 2:
            #    SALIDA = 1
        elif seleccionModulo == 3:
            moduloReportes()
            

def bienvenida():
    #Bienvenida
    print("Bienvenido a envíos Fidélitas express")
    print("Somos una empresa de hacer envios donde usted los necesite \n")
    
def menuModulos():
    print("Contamos con las siguientes opciones para usted: \n")
    print("1. Módulo de Envío")
    print("2. Módulo de Facturación")
    print("3. Módulo de Informes\n")
    
def moduloEnvio():
    SALIDA = 0
    print("Ingrese sus datos para continuar: ")
    informacionUsuario = solicitarInformacionParaEnvio()
    imprimirGeneralidadesEnvio()
    while SALIDA < 2:
        menuModalidadesEnvio()
        global identificador_paquete
        global listaPedidos
        identificador_paquete +=1
        """"""
        print("Número de pedido: ", identificador_paquete)
        global modalidad_seleccionada
        modalidad_seleccionada = int(input("\nSeleccione el número de la modalidad de envío: ")) 

        if modalidad_seleccionada <= 3:
                global peso_paquete     
                peso_paquete = float(input("Ingrese el Peso(kg) del paquete: "))
                if peso_paquete <= float(PESO_MAXIMO):

                    if modalidad_seleccionada == 1:
                        print("\nSe aplicará el cargo de ₡200 por Kg")
                        global costo_por_kilogramo
                        costo_por_kilogramo = COSTO_INICIAL + (MODULO_EXPRESS * (peso_paquete - REDUCCION_PESO))
                        print("El costo por el envío del paquete es de:", "₡", costo_por_kilogramo)
                        copiaInformacionUsuario = informacionUsuario[:]
                        copiaInformacionUsuario.insert(0, identificador_paquete)
                        copiaInformacionUsuario.append("Express")
                        copiaInformacionUsuario.append(costo_por_kilogramo)
                        copiaInformacionUsuario.append(peso_paquete)
                        #print(f"copia Informacion Usuario: {copiaInformacionUsuario}")
                        #print(f"información usuario: {informacionUsuario}")
                        #Crear una instancia para guardar los datos generales
                        #
                        listaPedidos.append(copiaInformacionUsuario)
                        print(listaPedidos)
                        print("\nSu envio fue registrado")
                        print("Desea ingresar otro pedido?")
                        SALIDA = int(input("1 = Si / 2 = No \n"))
                        

                    elif modalidad_seleccionada == 2:
                        print("\nSe aplicará el cargo de ₡100 por Kg")
                        costo_por_kilogramo = COSTO_INICIAL + (MODULO_BAJO_COSTO * (peso_paquete - REDUCCION_PESO))
                        print("El costo por el envío del paquete es de:", "₡", costo_por_kilogramo)
                        copiaInformacionUsuario2 = informacionUsuario[:]
                        copiaInformacionUsuario2.insert(0, identificador_paquete)
                        copiaInformacionUsuario2.append("Bajo costo")
                        copiaInformacionUsuario2.append(costo_por_kilogramo)
                        copiaInformacionUsuario2.append(peso_paquete)
                        #print(f"copia Informacion Usuario: {copiaInformacionUsuario2}")
                        #print(f"información usuario: {informacionUsuario}")
                        listaPedidos.append(copiaInformacionUsuario2)
                        print(listaPedidos)
                        print("\nSu envio fue registrado")
                        print("Desea ingresar otro pedido?")
                        SALIDA = int(input("1 = Si / 2 = No \n"))

                    elif modalidad_seleccionada == 3:
                        print("\nSe aplicará el cargo de ₡300 por Kg")
                        costo_por_kilogramo = COSTO_INICIAL + (MODULO_INTERNACIONAL * (peso_paquete - REDUCCION_PESO))
                        print("El costo por el envío del paquete es de:", "₡", costo_por_kilogramo)
                        copiaInformacionUsuario3 = informacionUsuario[:]
                        copiaInformacionUsuario3.insert(0, identificador_paquete)
                        copiaInformacionUsuario3.append("Internacional")
                        copiaInformacionUsuario3.append(costo_por_kilogramo)
                        copiaInformacionUsuario3.append(peso_paquete)
                        #print(f"copia Informacion Usuario: {copiaInformacionUsuario3}")
                        #print(f"información usuario: {informacionUsuario}")
                        listaPedidos.append(copiaInformacionUsuario3)
                        print(listaPedidos)
                        print("\nSu envio fue registrado")
                        print("Desea ingresar otro pedido?")
                        SALIDA = int(input("1 = Si / 2 = No \n")) 
                else:            
                    print("El peso máximo permitido son 45 kg")
        else:
            print('Opción ingresada no es válida\n')     
    else:
            print("Muchas gracias por realizar el envio con nosotros \n")


#Función para guardar los datos ingresados por el usuario
def solicitarInformacionParaEnvio():
    global nombre
    nombre = input("Ingrese el nombre completo de quien realiza el pedido: ")
    global identificación
    identificación = int(input("Identificación: "))
    global empresa
    empresa = input("Empresa donde labora: ")
    informacionPersona = [nombre,identificación,empresa]
    return informacionPersona


def imprimirGeneralidadesEnvio():
    print("\nSe cuenta con 3 modalidades de envío:")     
    print("Express")
    print("Bajo costo")
    print("Internacional\n")
    #Imprimir costos de los envios
    print("Cada paquete tiene un costo inicial de ₡1000 por el primer Kg.")
    print("Costo por Kilogramo adicional según la modalidad seleccionada: \n")
    
    
def menuModalidadesEnvio():
    print("1. Express: ₡200 por kilogramo")
    print("2. Bajo costo: ₡100 por kilogramo")
    print("3. Internacional: ₡300 por kilogramo\n")
    

def moduloFacturacion():
    ingresoCedula = int(input("Para brindar el detalle de sus pedidos, por favor ingrese su número de cédula: "))
    nombreEmpresa =(input("Ingrese el nombre de la empresa que desea la factura: "))
    direccion = (input("Ingrese la dirección de la empresa: "))
    telefono = int(input("Ingrese el número de telefono: "))

    print("------------------------------")
    print("\nFidélitas express")
    print("Cédula jurídica 3-101-400635")
    print("La aurora, Heredia, Costa Rica")
    print("https://ufidelitas.ac.cr/")
    print("506 2206-8600")
    print("------------------------------")
    print(nombreEmpresa)
    print(direccion)
    print(telefono)
    print("------------------------------")
    
    pedidosPorUsuario(ingresoCedula)
    

def pedidosPorUsuario(ingresoCedula):
    contadorFila = 0
    listaTemporal = []
    print("El detalle de sus pedidos se muestra a continuación: \n")
    print("Número de pedido, ","Nombre de quién realizó el pedio, ", "Compañía "," Monto por pedido \n")
    for contadorFila in range(len(listaPedidos)):  
        if ingresoCedula == listaPedidos[contadorFila][2]:
            listaTemporal.append(listaPedidos[contadorFila])
    
    if listaTemporal == []:
        print("Aún no ha ingresado ningún pedido")
    else:
        print(*listaTemporal,sep="\n")
        print("\n")
    sumaPedidoUsuario = sumaTotalPedido(listaTemporal)
    print(sumaPedidoUsuario)

def sumaTotalPedido(item):
    sumaTotal = 0
    print("La suma de todos los envios es: ")
    for contadorFila in range(len(item)):       
        sumaTotal += item[contadorFila][5]
    return sumaTotal      

"""

Este es el comienzo del módulo para la generación de reportes

"""

def moduloReportes():
    print("\n")
    print("1. Lista de paquetes creados")
    print("2. Resumen de ganancia")
    print("3. Cantidad de paquetes por rango de peso")
    decision = int(input("Por favor seleccione alguna de las opciones anteriores: "))
    if decision == 1:
        agregarInformacionPedidos()
        lecturaArchivo('Lista de paquetes creados.txt')
    if decision == 2:
        reporteGanancias()
    if decision == 3:
        reportePesoDePaquetes()
        lecturaArchivo("Reporte de peso de paquetes.txt")

"""Aquí se encuentran las funciones para el manejo de archivos"""

"""Función para agregar la información de pedidos"""

def agregarInformacionPedidos():
    
    """BUSQUEMOS CÓMO ITERAR SOBRE EL ARREGLO E IMPRIMIR LOS DATOS ACÁ"""
    
    archivoTemporal = abrirArchivo("Reporte de paquetes creados.txt", "a")
    for fila in listaPedidos:
        archivoTemporal.write("Información del pedido:")
        archivoTemporal.write("\n\n")
        archivoTemporal.write(f"Nombre = {str(fila[1])}")
        archivoTemporal.write("\n")
        archivoTemporal.write(f"Identificación = {str(fila[2])}")
        archivoTemporal.write("\n")
        archivoTemporal.write(f"Empresa = {str(fila[3])}")
        archivoTemporal.write("\n\n")
        archivoTemporal.write(f"Paquete #{str(fila[0])}")
        archivoTemporal.write("\n")
        archivoTemporal.write(f"Modalidad seleccionada = {str(fila[4])}")
        archivoTemporal.write("\n")
        archivoTemporal.write(f"Costo por el envio del paquete = {str(fila[5])}")
        archivoTemporal.write("\n")
        archivoTemporal.write(f"Peso del paquete Kg = {str(fila[6])}")
        archivoTemporal.write("\n\n")
        #print("\nLa información fue grabada correctamente")
    cerrarArchivo(archivoTemporal)

"""Función para abrir archivos"""           

def abrirArchivo(nombreArchivo,modo):
    archivoTemporal = open(nombreArchivo,modo,encoding='latin-1')
    return archivoTemporal

"""Función para cerrar archivos """

def cerrarArchivo(nombreArchivo):
    nombreArchivo.close()
  
"""Función para leer archivos"""
  
def lecturaArchivo(nombreArchivo):
    archivoTemporal = open(nombreArchivo,'r',encoding='latin-1')
    print(archivoTemporal.read())

def reporteGanancias():
    print('1')

def reportePesoDePaquetes():
    archivoTemportal = abrirArchivo("Reporte de peso de paquetes.txt", "a")
    archivoTemportal.write("Peso de los pedidos:")
    archivoTemportal.write("\n\n")

    for pedido in listaPedidos:  
        if pedido[6] != 0:
            archivoTemportal.write(str(pedido) + "\n")       
    archivoTemportal.write("\n")
    cerrarArchivo(archivoTemportal)



flujoPrincipalProyecto()