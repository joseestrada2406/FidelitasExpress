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
    bienvenida()
    while SALIDA == 0:
        menuModulos()
        seleccionModulo = int(input("Seleccione el módulo al que desea acceder: "))
        if seleccionModulo == 1:
            moduloEnvio()
        if seleccionModulo ==2:
            moduloFacturacion()
            
    

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
        modalidad_seleccionada = int(input("\nSeleccione el número de la modalidad de envío: ")) 
        if modalidad_seleccionada <= 3:
                peso_paquete = float(input("Ingrese el Peso(kg) del paquete: "))
                if peso_paquete <= float(PESO_MAXIMO):
                    if modalidad_seleccionada == 1:
                        print("\nSe aplicará el cargo de ₡200 por Kg")
                        costo_por_kilogramo = COSTO_INICIAL + (MODULO_EXPRESS * (peso_paquete - REDUCCION_PESO))
                        print("El costo por el envío del paquete es de:", "₡", costo_por_kilogramo)
                        copiaInformacionUsuario = informacionUsuario[:]
                        copiaInformacionUsuario.insert(0, identificador_paquete)
                        copiaInformacionUsuario.append("Express")
                        copiaInformacionUsuario.append(costo_por_kilogramo)
                        print(f"copia Informacion Usuario: {copiaInformacionUsuario}")
                        print(f"información usuario: {informacionUsuario}")
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
                        print(f"copia Informacion Usuario: {copiaInformacionUsuario2}")
                        print(f"información usuario: {informacionUsuario}")
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
                        print(f"copia Informacion Usuario: {copiaInformacionUsuario3}")
                        print(f"información usuario: {informacionUsuario}")
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
    nombre = input("Ingrese el nombre completo de quien realiza el pedido: ")
    identificación = int(input("Identificación: "))
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
    pedidosPorUsuario(ingresoCedula)
    

def pedidosPorUsuario(ingresoCedula):
    contadorFila = 0
    listaTemporal = []
    print("\nEl detalle de sus pedidos se muestra a continuación: \n")
    print("\nNúmero de pedido, ","Nombre de quién realizó el pedio, ", "Compañía "," Monto por pedido \n")
    for contadorFila in range(len(listaPedidos)):  
        if ingresoCedula == listaPedidos[contadorFila][2]:
            listaTemporal.append(listaPedidos[contadorFila])
    else: 
        print("Aún no ha ingresado ningún pedido")
    print(*listaTemporal,sep="\n")
    print("\n")
    
flujoPrincipalProyecto()