import uuid
# Tabla de procesos simulada
process_table = []

# Estados posibles para los procesos
PROCESS_STATES = ["Listo", "Ejecutando", "Bloqueado"]

# Función para mostrar el menú interactivo
def show_menu():
    print("\n===== SISTEMA OPERATIVO SIMULADO =====")
    print("1. Crear proceso")
    print("2. Mostrar procesos")
    print("3. Modificar estado de un proceso")
    print("4. Eliminar proceso")
    print("5. Salir")

# Función para crear un nuevo proceso
def create_process():
    process_id = str(uuid.uuid4())[:8]  # Genera un ID único para el proceso
    state = "Listo"
    priority = input("Ingrese la prioridad del proceso (1-10): ")

    # Validación de entrada
    if not priority.isdigit() or not (1 <= int(priority) <= 10):
        print("Prioridad no válida. Intente nuevamente.")
        return

    # Añadir el proceso a la tabla
    process = {
        "PID": process_id,
        "Estado": state,
        "Prioridad": int(priority)
    }
    process_table.append(process)
    print(f"Proceso {process_id} creado exitosamente con estado '{state}'.")

# Función para mostrar todos los procesos
def show_processes():
    if not process_table:
        print("No hay procesos en la tabla.")
        return

    print("\n===== TABLA DE PROCESOS =====")
    print(f"{'PID':<10} {'Estado':<15} {'Prioridad':<10}")
    print("-" * 40)
    for process in process_table:
        print(f"{process['PID']:<10}{process['Estado']:<15}{process['Prioridad']:<10}")

# Función para modificar el estado de un proceso
def modify_process_state():
    pid = input("Ingrese el PID del proceso a modificar: ")
    for process in process_table:
        if process["PID"] == pid:
            print("Estados disponibles: ", ", ".join(PROCESS_STATES))
            new_state = input("Ingrese el nuevo estado: ")
            if new_state in PROCESS_STATES:
                process["Estado"] = new_state
                print(f"Estado del proceso {pid} actualizado a '{new_state}'.")
            else:
                print("Estado no válido.")
            return
    print("PID no encontrado.")

# Función para eliminar un proceso
def delete_process():
    pid = input("Ingrese el PID del proceso a eliminar: ")
    global process_table
    process_table = [process for process in process_table if process["PID"] != pid]
    print(f"Proceso {pid} eliminado.")

# Función principal del sistema operativo simulado
def main():
    while True:
        show_menu()
        choice = input("Seleccione una opción: ")

        if choice == "1":
            create_process()
        elif choice == "2":
            show_processes()
        elif choice == "3":
            modify_process_state()
        elif choice == "4":
            delete_process()
        elif choice == "5":
            print("Saliendo del sistema operativo simulado. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecución del programa
if __name__ == "__main__":
    main()