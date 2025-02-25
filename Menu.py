import uuid
2	
3	# Tabla de procesos simulada
4   process_table = []
5	
6	# Estados posibles para los procesos
7	PROCESS_STATES = ["Listo", "Ejecutando", "Bloqueado"]
8	
9	# Función para mostrar el menú interactivo
10	def show_menu():
11	    print("\n===== SISTEMA OPERATIVO SIMULADO =====")
12	    print("1. Crear proceso")
13	    print("2. Mostrar procesos")
14	    print("3. Modificar estado de un proceso")
15	    print("4. Eliminar proceso")
16	    print("5. Salir")
17	
18	# Función para crear un nuevo proceso
19	def create_process():
20	    process_id = str(uuid.uuid4())[:8]  # Genera un ID único para el proceso
21	    state = "Listo"
22	    priority = input("Ingrese la prioridad del proceso (1-10): ")
23	
24	    # Validación de entrada
25	    if not priority.isdigit() or not (1 <= int(priority) <= 10):
26	        print("Prioridad no válida. Intente nuevamente.")
27	        return
28	
29	    # Añadir el proceso a la tabla
30	    process = {
31	        "PID": process_id,
32	        "Estado": state,
33	        "Prioridad": int(priority)
34	    }
35	    process_table.append(process)
36	    print(f"Proceso {process_id} creado exitosamente con estado '{state}'.")
37	
38	# Función para mostrar todos los procesos
39	def show_processes():
40	    if not process_table:
41	        print("No hay procesos en la tabla.")
42	        return
43	
44	    print("\n===== TABLA DE PROCESOS =====")
45	    print(f"{'PID':<10} {'Estado':<15} {'Prioridad':<10}")
46	    print("-" * 40)
47	    for process in process_table:
48	        print(f"{process['PID']:<10}{process['Estado']:<15}{process['Prioridad']:<10}")
49	
50	# Función para modificar el estado de un proceso
51	def modify_process_state():
52	    pid = input("Ingrese el PID del proceso a modificar: ")
53	    for process in process_table:
54	        if process["PID"] == pid:
55	            print("Estados disponibles: ", ", ".join(PROCESS_STATES))
56	            new_state = input("Ingrese el nuevo estado: ")
57	            if new_state in PROCESS_STATES:
58	                process["Estado"] = new_state
59	                print(f"Estado del proceso {pid} actualizado a '{new_state}'.")
60	            else:
61	                print("Estado no válido.")
62	            return
63	    print("PID no encontrado.")
64	
65	# Función para eliminar un proceso
66	def delete_process():
67	    pid = input("Ingrese el PID del proceso a eliminar: ")
68	    global process_table
69	    process_table = [process for process in process_table if process["PID"] != pid]
70	    print(f"Proceso {pid} eliminado.")
71	
72	# Función principal del sistema operativo simulado
73	def main():
74	    while True:
75	        show_menu()
76	        choice = input("Seleccione una opción: ")
77	
78	        if choice == "1":
79	            create_process()
80	        elif choice == "2":
81	            show_processes()
82	        elif choice == "3":
83	            modify_process_state()
84	        elif choice == "4":
85	            delete_process()
86	        elif choice == "5":
87	            print("Saliendo del sistema operativo simulado. ¡Adiós!")
88	            break
89	        else:
90	            print("Opción no válida. Intente nuevamente.")
91	
92	# Ejecución del programa
93	if __name__ == "__main__":
94	    main()
