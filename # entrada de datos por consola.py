# Ejercicio de practica con input
print("Bienvenidos al sistemas de empleados")
nombre = input("Ingrese el nombre del empleado: ")
print("El empleado es:", nombre)
edad = int(input("Ingrese la edad del empleado: "))
print("La edad del empleado es:", edad)
salario = float(input("Ingrese el salario del empleado: "))
print("El salario del empleado es:", salario)
esJefe = input("Ingrese 1 si el empleado es jefe, 0 si no lo es: ")
#comvertirlo en booleano
esJefe = esJefe.lower() in ['1', 'true', 'si', 'sí', 's']
print("¿El empleado es jefe?:", esJefe)
print ("por lo tanto el empleado", nombre, "tiene", edad, "años,", "gana", salario, "y su condición de jefe es", esJefe)
