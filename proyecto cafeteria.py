#repositorio
def menu(): 

    print("\n---Menú---")
    print("1.Ordenar una bebida")
    print("2.Ver total acumulado")
    print("3.Salir y pagar")
    
    opcion = int(input("Selecciona una opción: "))
    return opcion

def tamaño(tamaño_vaso): #definir una función
    
    # se definen datos para comenzar a crear la orden
    continuar = True    # Para condicionar que el while se repita a menos que se ponga lo contrario
    while continuar:
        if tamaño_vaso == 1:   #condicional
            opcion_vaso = "Vaso tamaño chico."
            continuar = False    # Para que el bucle acabe 
        elif tamaño_vaso == 2:
            opcion_vaso = "Vaso tamaño mediano."
            continuar = False
        elif tamaño_vaso == 3:
            opcion_vaso = "Vaso tamaño grande."
            continuar = False
        else:
            print("Ese tamaño no existe.")   # El bucle continua hasta que se elija una opción válida
            tamaño_vaso = int(input("Elija otra opcion: "))
    return opcion_vaso   # para que regrese el texto al final dependiendo la elección
            
        
def base(base_bebida):
      
    continuar = True   
    while continuar:    
        if base_bebida == 1:
            opcion_base = "Base leche lactosada."
            continuar = False
        elif base_bebida == 2:
            opcion_base = "Base leche deslactosada."
            continuar = False
        elif base_bebida == 3:
            opcion_base = "Base agua."
            continuar = False
        else:
            print ("Esa opcion no existe.")
            base_bebida = int(input("elija otra opcion: "))
    return opcion_base

def cafe(eleccion_cafe):
    
    if eleccion_cafe == 1:
        opcion_cafe = "Café cafeinado."
    else:
        opcion_cafe = "Café descafeinado."
    return opcion_cafe
        
def shots_cafe(cantidad_de_shots):
    
    continuar = True
    while continuar:
        if cantidad_de_shots == 1:
            cargas_cafe = ("Una carga de café.")
            continuar = False
        elif cantidad_de_shots == 2:
            cargas_cafe = ("Dos cargas de café.")
            continuar = False
        elif cantidad_de_shots == 3:
            cargas_cafe = ("Tres cargas de café.")
            continuar = False
        else:
            print("No se puede agregar más cargas.")
            cantidad_de_shots = int(input("Elija otra opcion: "))
    return cargas_cafe
            
def cargas_azucar(cantidad_de_azucar):
    continuar = True
    while continuar:
        if cantidad_de_azucar == 0:
            azucar = "Cero cargas de azúcar"
            continuar = False
        elif cantidad_de_azucar == 1:
            azucar = "Una carga de azúcar."
            continuar = False
        elif cantidad_de_azucar == 2:
            azucar =  "Dos cargas de azúcar."
            continuar = False
        elif cantidad_de_azucar == 3:
            azucar =  "Tres cargas de azúcar."
            continuar = False
        else:
            print("No se puede agregar más cargas.")
            cantidad_de_azucar = int(input("Elija otra opcion: "))
    return azucar
    
def crema(eleccion_crema):
    
    if eleccion_crema == 1:
        agregar_crema = "Agregaste crema."
    else:
        agregar_crema = "No agregaste crema."
    return agregar_crema
    
def main():
    
    nombre = input("\nBienvenid@, cuál es tu nombre?: ").upper() #su nombre se mostrará todo en mayúsculas como algunas cafeterías hacen
    
    total_acumulado = 0 #va a ir acumulando el total por cada vez que decida seguir pidiendo otra bebida y de esta manera será más fácil mostrar el total de todo al final
    opcion = 0
    
    historial_bebidas = [] #para agrupar todas las elecciones que hizo el usuario para su bebida
    
    while opcion !=3: #se repetirá el ciclo hasta que el usuario elija el 3, donde se saldrá del bucle. de esta manera podrá seguir pidiendo si desea
        opcion=menu()
        
        match opcion:
            case 1:
                print(f"\nBebida para {nombre}")
                
                tamaño_vaso = int(input("\nElija su tamaño de vaso: 1. chico, 2. mediano, 3. grande: ")) # Para que inserte un número. Es con el que elegirá lo que lleve su pedido
                resultado_tamaño = tamaño(tamaño_vaso)
                precio_vasos=[5,10,15]
                precio_vaso=precio_vasos[tamaño_vaso-1] #para que dependiendo la elección del usuario, el programa busque correctamente el número elegido de la lista de tamaños para dar el costo
                
                base_bebida = int(input("\nElija su tipo de base: 1. leche lactosada, 2. deslactosada o 3. agua: "))
                resultado_base = base(base_bebida)
                precio_bases=[10,15,5]
                precio_base=precio_bases[base_bebida-1]
                
                eleccion_cafe = int(input("\nElija su tipo de cafe: 1. cafeinado o 2. descafeinado: "))
                resultado_cafe = cafe(eleccion_cafe)
                
                cantidad_de_shots = int(input("\n¿Cuántos shots de café desea? (1-3): "))
                resultado_shots = shots_cafe(cantidad_de_shots)
                precio_shots=[0, 10, 20]
                precio_shot=precio_shots[cantidad_de_shots-1]
                
                cantidad_de_azucar = int(input("\n¿Cuántas cargas de azúcar desea? (1-3): "))
                resultado_cargas = cargas_azucar(cantidad_de_azucar)
                
                eleccion_crema = int(input("\nDesea agregar crema? (1. sí, 2. no): "))
                resultado_crema = crema(eleccion_crema)
                precios_crema=[15,0]
                precio_crema=precios_crema[eleccion_crema-1]
                
                total=precio_vaso + precio_base + precio_shot + precio_crema
                total_acumulado += total

                print("\n---Resumen de pedido--- ")
                if (base_bebida == 1 or base_bebida == 2) and (eleccion_cafe == 1 or eleccion_cafe== 2): # Condicionar en qué aplica para que la respuesta sea una u otra
                    print("\nTu bebida es un latte") # si se cumple mostrará que la bebida es un latte
                else:
                    print("\nTu bebida es un americano") # si no se cumple se mostrará que es un americano
                print(resultado_tamaño) # Al final se mandan a llamar todas las funciones que fueron definidas para mostrar los resultados
                print(resultado_base)
                print(resultado_cafe)
                print(resultado_shots)
                print(resultado_cargas)
                print(resultado_crema)
                print(f"El total de esta bebida es: ${total}")
                
                bebida = [resultado_tamaño, resultado_base, resultado_cafe, resultado_shots, resultado_cargas, resultado_crema] #guarda los detalles de la bebida actual para luego agregarla al historial
                historial_bebidas.append(bebida) #agrega la lista de la bebida que acaba de pedir y la junta con sus otros pedidos en el historial, de tal manera que al final pueda ver la cantidad de bebidas que ordenó
                
            case 2:
                print(f"El total acumulado de tu pedido es: ${total_acumulado}")
            
            case 3:
                print(f"Gracias por tu compra {nombre}, tu total a pagar es de: ${total_acumulado}")
                print(f"Total de bebidas: {len(historial_bebidas)}") #cuenta cuantas listas de bebidas se guardaron para devolver la cantidad de bebidas que pidió el usuario
                
            case _:
                print(f"Opción no válida, por favor elija 1, 2 o 3")

    
main()


    