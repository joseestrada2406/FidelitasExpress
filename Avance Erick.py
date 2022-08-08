from glob import glob


COSTO_INICIAL = 1000
PESO_MAXIMO = 45
MODULO_EXPRESS = 200
MODULO_BAJO_COSTO = 100
MODULO_INTERNACIONAL = 300
REDUCCION_PESO = 1
identificador_paquete = 0
listaPedidos = []

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
        if seleccionModulo == 2:
            moduloFacturacion()
            seleccionSeguir = int(input("Desea realizar otra operación: 1=Si / 2=No "))
            if seleccionSeguir == 2:
                SALIDA = 1
            

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


flujoPrincipalProyecto()




#Juanca

def crearArchivo():
    file = open("Lista de paquetes creados.txt", "w")
    file.close()

def agregarInformacion():
    file = open("Lista de paquetes creados.txt", "a")
    file.write("Información del pedido:")
    file.write("\n\n")
    file.write("Nombre = % s"%nombre)
    file.write("\n")
    file.write("Identificación = % s"%identificación)
    file.write("\n")
    file.write("Empresa = % s"%empresa)
    file.write("\n\n")
    file.write("Paquete # % s"%identificador_paquete)
    file.write("\n")
    file.write("Modalidad seleccionada = % s"%modalidad_seleccionada)
    file.write("\n")
    file.write("Costo por el envio del paquete = % s"%costo_por_kilogramo)
    file.write("\n")
    file.write("Peso del paquete Kg = % s"%peso_paquete)
    file.write("\n\n")
    print("\nLa información fue grabada correctamente")
    file.close()

def mostrarInformacion():
    file = open("Lista de paquetes creados.txt", "r")
    mensaje = file.read()
    print(mensaje)
    file.close()

def Adicional():
    SALIDA = 0
    if (SALIDA == 1):
        agregarInformacion()
       
if __name__=="__main__":
    Adicional()

crearArchivo()
mostrarInformacion()
agregarInformacion()

#Erick

def crearArchivoErick():
    file = open("Reporte de peso de paquetes.txt", "w")
    file.close()

def agregarInformacionErick():
    file = open("Reporte de peso de paquetes.txt", "a")
    file.write("Peso de los pedidos:")
    file.write("\n\n")

    for pedido in listaPedidos:  
        if pedido[6] != 0:
            file.write(str(pedido) + "\n")       
    file.write("\n")
    
    print("\nLa información fue grabada correctamente")
    file.close()

def mostrarInformacionErick():
    file = open("Reporte de peso de paquetes.txt", "r")
    mensaje = file.read()
    print(mensaje)
    file.close()

def Adicional():
    SALIDA = 0
    if (SALIDA == 1):
        agregarInformacionErick()
       
if __name__=="__main__":
    Adicional()

crearArchivoErick()
agregarInformacionErick()
mostrarInformacionErick()