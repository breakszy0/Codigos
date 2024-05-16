import os

def calcular_liquidacion():
    # Ingreso de datos del trabajador
    nombre_trabajador = input("Ingrese el nombre del trabajador: ")
    if not nombre_trabajador.strip():
        print("El nombre del trabajador no puede estar vacío.")
        return
    elif len(nombre_trabajador) > 30:
        print("El nombre debe tener entre 1 y 30 caracteres.")
        return

    try:
        sueldo_base = float(input("Ingrese el sueldo base: "))
        horas = float(input("Ingrese el número de horas trabajadas: "))
    except ValueError:
        print("El sueldo base y las horas deben ser valores numéricos positivos.")
        return

    if sueldo_base < 0 or horas < 0:
        print("El sueldo base y las horas deben ser valores numéricos positivos.")
        return
    elif horas > 180:
        print("No puedes trabajar más de 180 horas por mes.")
        return

    # Cálculos
    pago_horas = horas * (sueldo_base / 180) * 1.5
    total_ingresos = sueldo_base + pago_horas
    fonasa = total_ingresos * 0.07
    afp = total_ingresos * 0.10
    sueldo_neto = total_ingresos - (fonasa + afp)

    # Mostrar la liquidación
    print("\nLiquidación de sueldo para", nombre_trabajador)
    print(f"Sueldo base: ${sueldo_base:.0f}")
    print(f"Pago por horas: ${pago_horas:,.0f}")
    print(f"Total de ingresos: ${total_ingresos:,.0f}")
    print(f"Descuento por Fonasa: ${fonasa:,.0f}")
    print(f"Descuento por AFP: ${afp:,.0f}")
    print(f"Sueldo neto a pagar: ${sueldo_neto:,.0f}")

    carpeta_nombre = f"liquidacion_{nombre_trabajador}"
    os.makedirs(carpeta_nombre, exist_ok=True)

    # Guardar la liquidación en un archivo de texto
    archivo_nombre = f"{carpeta_nombre}/liquidacion_{nombre_trabajador}.txt"
    with open(archivo_nombre, "w") as archivo:
        archivo.write(f"Liquidación de sueldo para {nombre_trabajador}\n")
        archivo.write(f"Sueldo base: ${sueldo_base:.0f}\n")
        archivo.write(f"Pago por horas: ${pago_horas:,.0f}\n")
        archivo.write(f"Total de ingresos: ${total_ingresos:,.0f}\n")
        archivo.write(f"Descuento por Fonasa: ${fonasa:,.0f}\n")
        archivo.write(f"Descuento por AFP: ${afp:,.0f}\n")
        archivo.write(f"Sueldo neto a pagar: ${sueldo_neto:,.0f}\n")

    print(f"\nSe ha creado la carpeta '{carpeta_nombre}' y el archivo '{archivo_nombre}'.")
    return

# Ejecutar la función
calcular_liquidacion()
