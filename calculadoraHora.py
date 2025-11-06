def calculadora_tiempo():
    print("=== Calculadora de Horas y Minutos ===")
    print("Ingresa los tiempos uno por uno (ejemplo: 1h 30m o 45m).")
    print("Cuando termines, escribe 'fin' para obtener el resultado.\n")

    total_minutos = 0

    while True:
        entrada = input("Tiempo: ").lower().strip()
        if entrada == "fin":
            break

        horas = 0
        minutos = 0

        # Buscar horas
        if "h" in entrada:
            try:
                partes = entrada.split("h")
                horas = int(partes[0].strip())
                entrada = partes[1]
            except:
                horas = 0

        # Buscar minutos
        if "m" in entrada:
            try:
                minutos = int(entrada.split("m")[0].strip())
            except:
                minutos = 0

        total_minutos += horas * 60 + minutos

    # Convertir a formato horas:minutos
    horas_final = total_minutos // 60
    minutos_final = total_minutos % 60

    print("\n=== Resultado Total ===")
    print(f"{horas_final} horas y {minutos_final} minutos")
    print("========================")

# Ejecutar
calculadora_tiempo()
