boletos={"1":["funcion cats dia viernes",150],"2":["funcion cats dia sabado",180]}
compradores={}
def validarUsuario(nombre):
    if nombre in compradores:
        return True
    else: 
        return False
def comprarentrada(nombre):
    print("-- seleccione la funcion --")
    print("1. funcion dia: ",boletos["1"][0], "stock disponible: ",boletos["1"][1])
    print("2. funcion dia: ",boletos["2"][0], "stock disponible: ",boletos["2"][1])
    opcion=int(input("ingrese su opcion: "))
    if(opcion==1 and boletos["1"][1]>0):
        compradores[nombre]={"funcion":boletos["1"][0]}
        boletos["1"][1]=boletos["1"][1] - 1
        print ("compra registrada en la ",boletos["1"][0], "el stock actual es: ",boletos["1"][1])
    elif(opcion==2 and boletos["2"][1]>0):
        compradores[nombre]={"funcion":boletos["2"][0]}
        boletos["2"][1]=boletos["2"][1] - 1
        print ("compra registrada en la ",boletos["2"][0], "el stock actual es: ",boletos["2"][1])
    else:
        print("opcion no valida...")

def cambiofuncion(nombre):
    if validarUsuario(nombre):
        dia=""
        print("ud posee la entrada para el dia", compradores[nombre]["funcion"])
        for i in boletos.values():
            if(i[0] == compradores[nombre]["funcion"]):
                continue
            else:
                
                print("desea cambiar su boleto para el dia",i[0])
                op=int(input("1-si \n2- no \ningrese opcion: "))
                if(op==1 and i[1]>0):
                    dia = compradores[nombre]["funcion"]
                    compradores[nombre]["funcion"] = i[0]
                    i[1]=i[1]-1
                    print(compradores)
                    for j in boletos.values():
                        if(j[0]==dia):
                            j[1]=j[1]+1
                    break
                elif(op==1 and i<=0):
                    print("no quedan boletos para esa funcion ")
                    break
                elif(op==2):
                    print("no se genero el cambio...")
                else:
                    print("opcion no valida")
                    break
    else:
        print("usuario no encontrado")
    
def mostrarstock():
    print("________stock actual________")
    for i in boletos.values():
        print(i[0],i[1])

while (True):
    print("______TOTEM AUTOATENCIÓN CAFECONLECHE__________")
    try:
        opcion=int(input("1.- Comprar entrada a Cats. \n2.- Cambio de función. \n3.- Mostrar stock de funciones \n4.-salir\ningrese su opcion: "))
        if opcion==1:
            usuario=input("ingrese su nombre: ")
            if(validarUsuario(usuario)):
                print("el usuario ya existe...")
            else:
                comprarentrada(usuario)
        elif opcion==2:
            nombre=input("ingrese su nombre: ")
            cambiofuncion(nombre)
        elif opcion==3:
            mostrarstock()
        elif opcion==4:
            print("saliendo...")
            break
        else:
            print("opcion no valida...")
    except ValueError:
        print("ERROR ingrese un numero")

#terminado mas o menos