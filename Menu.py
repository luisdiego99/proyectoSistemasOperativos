import uuid
import datetime
import os
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
    print("5. Mostrar logs")
    print("6. Salir")

# Función para crear un nuevo proceso
def create_process():
    process_id = str(uuid.uuid4())[:8]  # Genera un ID único para el proceso
    state = "Listo"
    priority = input("Ingrese la prioridad del proceso (1-10): ")

    # Validación de entrada
    if not priority.isdigit() or not (1 <= int(priority) <= 10):
        print("\nPrioridad no válida. Intente nuevamente.")
        log_action(f"Intento de creación fallido: Prioridad de proceso fuera de rango")
        return

    # Añadir el proceso a la tabla
    process = {
        "PID": process_id,
        "Estado": state,
        "Prioridad": int(priority)
    }
    process_table.append(process)
    print(f"\nProceso {process_id} creado exitosamente con estado '{state}'.")
    log_action(f"Proceso creado: PID={process_id} con prioridad: {priority}") #Log agregado al log file

# Función para mostrar todos los procesos
def show_processes():
    if not process_table:
        print("\nNo hay procesos en la tabla.")
        log_action("La tabla de procesos ha sido consultada, pero se encuentra vacía")
        return
    print("\n===== TABLA DE PROCESOS =====")
    print(f"{'PID':<10} {'Estado':<15} {'Prioridad':<10}")
    print("-" * 40)
    log_action("La tabla de procesos ha sido consultada")
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
                print(f"\nEstado del proceso {pid} actualizado a '{new_state}'.")
                log_action(f"\nEstado del proceso {pid} actualizado a '{new_state}'.")
            else:
                print("\nEstado no válido.")
                log_action(f"Intento de modificación fallido: El estado {new_state} no es válido.")
            return
    print("\nPID no encontrado.")
    log_action(f"Intento de modificación fallido: No se encontro el proceso: {pid}")
# Función para eliminar un proceso
def delete_process():
    pid = input("Ingrese el PID del proceso a eliminar: ")
    global process_table
    process_table = [process for process in process_table if process["PID"] != pid]
    print(f"\nProceso {pid} eliminado.")
    log_action(f"Proceso {pid} eliminado.")
# Función para mostrar el registro de logs
def print_logs():  
    print("\n===== HISTORIAL DE LOGS =====")
    try:
        with open("system_log.txt", "r") as log_file:
            for line_number, line in enumerate(log_file, start=1):
                print(f"{line_number}: {line.strip()}")
    except FileNotFoundError:
        print("El archivo de logs no existe.")


# Función para registrar logs en un file
def log_action(action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("system_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {action}\n")
        #print("LOG ACTION FUE EJECUTADO")

# Función principal del sistema operativo simulado
def main():
    if not os.path.exists("system_log.txt"):
        print("Creando archivo de logs...")
    open("system_log.txt", "w").close()  # Clears the file at the beginning of the program
    while True:
        show_menu()
        choice = input("Seleccione una de las siguientes opciones: ")

        if choice == "1":
            create_process()
        elif choice == "2":
            show_processes()
        elif choice == "3":
            modify_process_state()
        elif choice == "4":
            delete_process()
        elif choice == "5":
            print_logs()
        elif choice == "6":
            print("\nSaliendo del sistema operativo simulado. ¡Adiós!")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

# Ejecución del programa
if __name__ == "__main__":
    main()