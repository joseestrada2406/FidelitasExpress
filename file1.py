listaPedidos = []

def agregarUsuarios(item):
    listaPedidos.append(item)
    

def solicitarInformacionParaEnvio():
    nombre = input("Nombre completo: ")
    identificación = int(input("Identificación: "))
    empresa = input("Empresa donde labora: ")
    informacionPersona = [nombre,identificación,empresa]
    print(informacionPersona)
    return informacionPersona


def pruebaLista():
    prueba = solicitarInformacionParaEnvio()
    #print(prueba)
    print(listaPedidos)
    valor = input("Ingrese el valor: ")
    prueba.insert(0, valor)
    agregarUsuarios(prueba)
    print(prueba)
    print(listaPedidos)
SALIDA =1    
prueba = solicitarInformacionParaEnvio()
while SALIDA < 2:
    opcion = int(input("Ingrese Opcion: "))
    if opcion ==1:
        print(listaPedidos)
        valor = input("Ingrese el valor: ")
        prueba.insert(0, valor)
        agregarUsuarios(prueba)
        print(prueba)
        print(listaPedidos)
    elif opcion == 2:
        print(listaPedidos)
        valor = input("Ingrese el valor: ")
        prueba.insert(0, valor)
        agregarUsuarios(prueba)
        print(prueba)
        print(listaPedidos)
    else:
        SALIDA +=1
        
        
