# def show_menu():
#     while True: 
#         print("\n===== SISTEMA OPERATIVO SIMULADO =====")
#         print("1. Crear proceso")
#         print("2. Mostrar procesos")
#         print("3. Modificar estado de un proceso")
#         print("4. Eliminar proceso")
#         print("5. Salir")

#         choice = input("Seleccione una opción: ")

#         if choice == "1":
#             create_process()
#         elif choice == "2":
#             show_processes()
#         elif choice == "3":
#             modify_process_state()
#         elif choice == "4":
#             delete_process()
#         elif choice == "5":
#             print("Saliendo del sistema operativo simulado. ¡Adiós!")
#             break
#         else:
#             print("Opción no válida. Intente nuevamente.")

# show_menu()

# Placeholder functions for demonstration
def create_process():
    print("Función 'crear proceso' ejecutada.")

def show_processes():
    print("Función 'mostrar procesos' ejecutada.")

def modify_process_state():
    print("Función 'modificar estado de un proceso' ejecutada.")

def delete_process():
    print("Función 'eliminar proceso' ejecutada.")

# Menu function
def show_menu():
    while True: 
        print("\n===== SISTEMA OPERATIVO SIMULADO =====")
        print("1. Crear proceso")
        print("2. Mostrar procesos")
        print("3. Modificar estado de un proceso")
        print("4. Eliminar proceso")
        print("5. Salir")

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

# Run the menu
show_menu()