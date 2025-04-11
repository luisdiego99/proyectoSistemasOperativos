          print(f"\nProceso {process['PID']} (Prioridad {process['Prioridad']}) ejecutando quantum de {time_this_iteration}s")

            if buffer_used + memory_this_iteration > self.buffer_size:
                print(f"\nProceso {process['PID']} BLOQUEADO - No hay suficiente memoria para ejecutarse")
                process["Estado"] = "Bloqueado"
                self.blocked_queue.append(process)
                return
            else:
                print(f"Proceso {process['PID']} ejecutando... usando {memory_this_iteration:.2f}KB de memoria")
                buffer_used += memory_this_iteration  # Simula el uso de memoria SIN tocar el buffer (lista)

            process["Remaining_Time"] -= time_this_iteration
            if process["Remaining_Time"] <= 0:
                process["Estado"] = "Terminado"
                print(f"Proceso {process['PID']} COMPLETADO")
                buffer_used -= memory_this_iteration  # Libera la memoria que estaba usando
            else:
                process["Estado"] = "Listo"
                print(f"Proceso {process['PID']} PAUSADO - {process['Remaining_Time']}s restantes")
                buffer_used -= memory_this_iteration  # Libera memoria temporalmente usada
                self.ready_queue.append(process)

                #time.sleep(1)
                process["Remaining_Time"] -= time_this_iteration
                if process["Remaining_Time"] <= 0:
                    process["Estado"] = "Terminado"
                    print(f"Proceso {process['PID']} COMPLETADO")
                else:
                    process["Estado"] = "Listo"
                    print(f"Proceso {process['PID']} PAUSADO - {process['Remaining_Time']}s restantes")
                    self.ready_queue.append(process)