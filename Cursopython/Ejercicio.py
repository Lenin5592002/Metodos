numeros = range(1, 10 + 1)

numeros_pares = []

# Forma tradicional
for num in numeros:
    if num % 2 == 0:
        numeros_pares.append(num)

print(f"Números pares del 1 al 10: {numeros_pares}")

# Con comprensión de listas
numeros_pares = [num for num in numeros if num % 2 == 0]
print(f"Números pares del 1 al 10 (comprensión): {numeros_pares}")
