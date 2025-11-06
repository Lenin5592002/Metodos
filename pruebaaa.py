import json
import os


ARCHIVO_TODO = "todo_list.json"


def cargar_actividades():
    if os.path.exists(ARCHIVO_TODO):
        with open(ARCHIVO_TODO, "r") as f:
            return json.load(f)
    return []


def guardar_actividades(actividades):
    with open(ARCHIVO_TODO, "w") as f:
        json.dump(actividades, f, indent=4)

def mostrar_actividades(actividades):
    if not actividades:
        print("\n No hay actividades pendientes. ¡Buen trabajo!")
    else:
        print("\n Lista de actividades pendientes:")
        for i, act in enumerate(actividades):
            print(f"{i+1}. {act['nombre']} {'' if act['completado'] else ''}")

def main():
    actividades = cargar_actividades()

    while True:
        mostrar_actividades([a for a in actividades if not a['completado']])

        print("\nOpciones:")
        print("1. Agregar nueva actividad")
        print("2. Marcar actividad como completada")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Escribe el nombre de la nueva actividad: ")
            actividades.append({"nombre": nombre, "completado": False})
            guardar_actividades(actividades)
            print(" Actividad agregada correctamente.")

        elif opcion == "2":
            pendientes = [a for a in actividades if not a['completado']]
            if not pendientes:
                print(" No hay actividades para marcar.")
                continue

            try:
                indice = int(input("Número de actividad a marcar como completada: ")) - 1
                if 0 <= indice < len(pendientes):
                    pendientes[indice]['completado'] = True
                    # Actualizar lista original
                    for act in actividades:
                        if act['nombre'] == pendientes[indice]['nombre']:
                            act['completado'] = True
                    guardar_actividades(actividades)
                    print(" Actividad marcada como completada.")
                else:
                    print("Número fuera de rango.")
            except ValueError:
                print("Por favor ingresa un número válido.")

        elif opcion == "3":
            print(" Saliendo del programa. ¡Hasta la próxima!")
            break

        else:
            print(" Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
