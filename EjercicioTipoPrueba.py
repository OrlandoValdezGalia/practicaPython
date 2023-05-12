precioEntrada, acumuladorEntradasMenores, acumuladorEntradasAdultos, acumuladorEntradasMayores, entradaAdulto, EntradaAdultoMayor, EntradaNino = 0, 0, 0, 0, 0, 0, 0
descuento = 0
subCostoMenores = 0
subCostoMayores = 0
subCostoAdultos = 0
subDescuentoTotal = 0
tipoEntrada = ""
i = 1

# 10 menores
# 5 adultos
# no aplica

print("---------- Bienvenido a Buena Aventura ----------")

while i == 1:
    print("1) Menores - $2500\n2) Adultos - $5000\n3) Adultos Mayores - $1000\n")
    opcionEntrada = int(input("Ingrese la entrada que desee: "))

    if  opcionEntrada > 0 and opcionEntrada < 4:

        if  opcionEntrada == 1:
            tipoEntrada = "Menores"
            precioEntrada = 2500            
            cantidadEntradas = int(input("¿Cuantas entradas desea?: "))
            acumuladorEntradasMenores += cantidadEntradas
            subCosto = precioEntrada * acumuladorEntradasMenores
            print("\nDesea escoger mas entradas?\n1) Si\n2) No\n")
            masEntradas = int(input("Escoja una opción: "))

            if  masEntradas > 0 and masEntradas < 3:
                if masEntradas == 1:
                    continue
            else:
                print("Opción elegida no es correcta.")

        elif opcionEntrada == 2:
            tipoEntrada = "Adultos"
            precioEntrada = 5000            
            cantidadEntradas = int(input("¿Cuantas entradas desea?: "))
            acumuladorEntradasAdultos += cantidadEntradas
            print("\nDesea escoger mas entradas?\n1) Si\n2) No\n")
            masEntradas = int(input("Escoja una opción: "))

            if  masEntradas > 0 and masEntradas < 3:
                if masEntradas == 1:
                    continue
            else:
                print("Opción elegida no es correcta.")
        
        elif opcionEntrada == 3:
            tipoEntrada = "Mayores"
            precioEntrada = 1000            
            cantidadEntradas = int(input("¿Cuantas entradas desea?: "))
            acumuladorEntradasMayores += cantidadEntradas
            print("\nDesea escoger mas entradas?\n1) Si\n2) No\n")
            masEntradas = int(input("Escoja una opción: "))

            if  masEntradas > 0 and masEntradas < 3:
                if masEntradas == 1:
                    continue
            else:
                print("Opción elegida no es correcta.")
        
        if acumuladorEntradasMenores > 0 or acumuladorEntradasAdultos > 0 or acumuladorEntradasMayores > 0:
            if acumuladorEntradasMenores > 0:                
                subCostoMenores = acumuladorEntradasMenores * 2500
            
            if acumuladorEntradasAdultos > 0:                
                subCostoAdultos = acumuladorEntradasAdultos * 5000 
            
            if acumuladorEntradasMayores > 0:                
                subCostoMayores = acumuladorEntradasMayores * 1000
        else:
            descuento = 0
            
        subCosto = subCostoMenores + subCostoAdultos + subCostoMayores
            
        print("\nEs viernes?\n1) Si\n2) No")
        esViernes = int(input("Ingrese una opcion: "))
        
        if esViernes == 1:
            if acumuladorEntradasMenores > 0 and acumuladorEntradasMayores > 0:
                subDescuentoTotal = subCosto * 15 / 100
            elif acumuladorEntradasMenores > 0 or acumuladorEntradasMayores > 0:
                if acumuladorEntradasMenores > 0:
                    descuento += 10
                    
                if acumuladorEntradasMayores > 0:
                    descuento += 5
                    
                subDescuentoTotal = subCosto * descuento / 100
        
        
        
        total = subCosto - subDescuentoTotal
        print("\n-------------------- Entradas --------------------")
        print(f"{acumuladorEntradasMenores} entradas de Menores: {subCostoMenores}")
        print(f"{acumuladorEntradasAdultos} entradas de Adultos: {subCostoAdultos}")
        print(f"{acumuladorEntradasMayores} entradas de Mayores: {subCostoMayores}")
        print("--------------------------------------------------")
        print(f"Subtotal - {subCosto}\nDescuento - {subDescuentoTotal}")
        print("--------------------------------------------------")
        print(f"Total a pagar: {total}\n")
        print("¡Gracias por su compra :)!")
        i = 0   
    
    else:
        print("La opcion elegida es incorrecta")
    
    