
COSTO_INICIAL = 1000
PESO_MAXIMO = 45
MODULO_EXPRESS = 200
MODULO_BAJO_COSTO = 100
MODULO_INTERNACIONAL = 300
REDUCCION_PESO = 1
#listaPedidos = [[1, 'Jose Estrada', 402310691, 'Experian', 'Express', 2800.0, 10.0],[2, 'Jose Estrada', 402310691, 'Experian', 'Express', 2800.0, 19.0],[3, 'Jose Estrada', 402310691, 'Experian', 'Express', 2800.0, 32.0],[4, 'Jose Estrada', 402310691, 'Experian', 'Bajo costo', 14000.0, 32.0]]
listaPedidos = []
identificador_paquete = 0
if (len(listaPedidos) > 0 ):
    identificador_paquete = int(listaPedidos[-1][0])
    
#Para paquetes con peso entre 1 a 10
rangoA = []
#Para paquetes con peso entre 11 a 20
rangoB = []
#Para paquetes con peso entre 21 a 30
rangoC = []
#Para paquetes con peso entre 31 a 45
rangoD = []
#Variables para obtener la ganancia por modalidad de envío
gananciaModExpress = 0
gananciaModBajoCosto = 0
gananciaModInternacional = 0


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
    """Flujo principal para el módulo de envío"""
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



def solicitarInformacionParaEnvio():
    """Función para guardar los datos ingresados por el usuario"""
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
    """Flujo principal del módulo de facturación"""
    ingresoCedula = int(input("Para brindar el detalle de sus pedidos, por favor ingrese su número de cédula: "))
    nombreEmpresa =(input("Ingrese el nombre de la empresa que desea la factura: "))
    direccion = (input("Ingrese la dirección de la empresa: "))
    telefono = int(input("Ingrese el número de telefono: "))

    print("------------------------------")
    print("\nFidélitas express")
    print("Cédula jurídica 3-101-400635")
    print("La aurora, Heredia, Costa Rica")
    print("https://urldefense.com/v3/__https://ufidelitas.ac.cr/__;!!MfzFaTml5A!m8mCD4-y7jHMSvG3bu6XaW-7Cf9qDh0nPyhhBNt8m_-zyNrnwsj7i27FK8sj5G-xvPrnjWFPGFXy8mMWHaalH52LekLpSQ$  ")
    print("506 2206-8600")
    print("------------------------------")
    print(nombreEmpresa)
    print(direccion)
    print(telefono)
    print("------------------------------")
    
    pedidosPorUsuario(ingresoCedula)
    

def pedidosPorUsuario(ingresoCedula):
    """Función para listar los pedidos realizados por usuarios"""
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
    """Flujo principal para el módulo de reportes"""
    print("\n")
    print("1. Lista de paquetes creados")
    print("2. Resumen de ganancia")
    print("3. Cantidad de paquetes por rango de peso")
    decision = int(input("Por favor seleccione alguna de las opciones anteriores: "))
    if decision == 1:
        agregarInformacionPedidos()
        lecturaArchivo('Reporte de paquetes creados.txt')
    if decision == 2:
        sumaPedidosSegunModalidad()
        reporteGanancias()
        lecturaArchivo("Reporte de ganancias.txt")
    if decision == 3:
        creacionDeRangosSegunPeso()
        escrituraArchivoRangos(rangoA,"Rango A","1 a 10 kgs")
        escrituraArchivoRangos(rangoB,"Rango B","11 a 20 kgs")
        escrituraArchivoRangos(rangoC,"Rango C","21 a 30 kgs")
        escrituraArchivoRangos(rangoD,"Rango D","31 a 45 kgs")
        lecturaArchivo("Archivo Rango A.txt")
        lecturaArchivo("Archivo Rango B.txt")
        lecturaArchivo("Archivo Rango C.txt")
        lecturaArchivo("Archivo Rango D.txt")


"""Aquí se encuentran las funciones para el manejo de archivos"""


def agregarInformacionPedidos():
    """Función para agregar la información de pedidos"""
    
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
    cerrarArchivo(archivoTemporal)

           
def abrirArchivo(nombreArchivo,modo):
    """Función para abrir archivos"""
    archivoTemporal = open(nombreArchivo,modo,encoding='latin-1')
    return archivoTemporal


def cerrarArchivo(nombreArchivo):
    """Función para cerrar archivos """
    nombreArchivo.close()
  
  
def lecturaArchivo(nombreArchivo):
    """Función para leer archivos"""
    archivoTemporal = open(nombreArchivo,'r',encoding='latin-1')
    print(archivoTemporal.read())
    cerrarArchivo(archivoTemporal)

def sumaPedidosSegunModalidad():
    """Función para calcular la ganancia de los pedidos según su modalidad"""
    global gananciaModExpress
    global gananciaModBajoCosto
    global gananciaModInternacional
    for fila in listaPedidos:
        if fila[4] == 'Express':
            gananciaModExpress += fila[5]
        elif fila[4] =='Bajo costo':
            gananciaModBajoCosto +=fila[5]
        else:
            gananciaModInternacional +=fila[5]      
    
def reporteGanancias():
    """Función para generar el reporte de ganancias"""
    global gananciaModExpress
    global gananciaModBajoCosto
    global gananciaModInternacional
    archivoTemporal = abrirArchivo(f"Reporte de ganancias.txt",'a')
    archivoTemporal.write(f"\nA continuación, se presenta el resumen de ganancias según la modalidad: \n\n")
    archivoTemporal.write(f"Modalidad Express: {gananciaModExpress}\n")
    archivoTemporal.write(f"Modalidad Bajo costo: {gananciaModBajoCosto}\n")
    archivoTemporal.write(f"Modalidad Internacional: {gananciaModInternacional}")
    cerrarArchivo(archivoTemporal)

def creacionDeRangosSegunPeso():
    """Función para separar los pedidos según sus rangos de peso después de truncarlos"""
    for pedido in listaPedidos:  
        if  0 < pedido[6] < 11:
            pedido[6] = int(pedido[6])
            rangoA.append(pedido)
        elif 11 <= pedido[6] < 21:
            pedido[6] = int(pedido[6])
            rangoB.append(pedido)
        elif 21 <= pedido[6] < 31:
            pedido[6] = int(pedido[6])
            rangoC.append(pedido)
        else:
            pedido[6] = int(pedido[6])
            rangoD.append(pedido)
            
def escrituraArchivoRangos(nombreLista,nombreRango,rango):
    """Funcion para escribir en el archivo para los Rangos"""
    archivoTemporal = abrirArchivo(f"Archivo {nombreRango}.txt",'a')
    archivoTemporal.write(f"\n{nombreRango}\n\n")
    archivoTemporal.write(f"Se cuentan con los siguientes pedidos con peso entre los {rango}: \n")
    for fila in nombreLista:
        archivoTemporal.write(f"Pedido #{fila[0]}\n")
        archivoTemporal.write(f"Modalidad = {fila[4]}\n")
        archivoTemporal.write(f"Peso ={fila[6]}\n")
    cerrarArchivo(archivoTemporal)
        



flujoPrincipalProyecto()