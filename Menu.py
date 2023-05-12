i = 1
subTotal = 0
print("------- Bienvenidos -------")
name = input("Ingrese su nombre: ")
lastName = input("Ingrese su apellido: ")


print("--- Que tipo de pan deseas ---")
print("1) Amasado - 1500\n2) Molde - 1000\n3) Baguette - 2000\n4) Integral - 3000\n")

while i == 1:
    opcionElegida = int(input("Elige una opción: "))
    CantidadPan = int(input("Seleccione la cantidad que desee: "))
    
    if opcionElegida > 0 and opcionElegida < 5:
        match opcionElegida:
            case 1:
                subTotal += 1500 * CantidadPan
                if  subTotal > 5000:
                    envio = 0 #Gratis
                    
                    print("Desea terminar el pedido:\n1) Si\n2) No")
                    opcionFinPedido = int(input("Ingrese una opcion: "))
                    
                    if opcionFinPedido == 1:
                        print("--- Boleta ---")
                        print(f"Nombre: {name}\nApellido: {lastName}\nSubTotal: {subTotal}\nTotal: {total}")
                        i = 0
                    else:
                        print("Que producto desea volver a elegir?\n")
                        print("1) Amasado - 1500\n2) Molde - 1000\n3) Baguette - 2000\n4) Integral - 3000\n")
                else:
                    envio = subTotal * 10 / 100
                    
                    print("Desea terminar el pedido:\n1) Si\n2) No")
                    opcionFinPedido = int(input("Ingrese una opcion: "))
                    
                    if opcionFinPedido == 1:
                        total = subTotal + envio
                        print("--- Boleta ---")
                        print(f"Nombre: {name}\nApellido: {lastName}\nSubTotal: {subTotal}\nTotal: {total}")
                        i = 0
                    else:
                        print("Que producto desea volver a elegir?\n")
                        print("1) Amasado - 1500\n2) Molde - 1000\n3) Baguette - 2000\n4) Integral - 3000\n")
                
            case 2: 
                subTotal += 1000 * CantidadPan
            case 3: 
                subTotal += 2000 * CantidadPan
            case 4: 
                subTotal += 3000 * CantidadPan