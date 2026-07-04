
import time
from lista_reparaciones import ListaReparaciones
from colores import Colores
from conversor import ConversorMoneda

def ejecutar_menu():
    sistema = ListaReparaciones()
    sistema.cargar_desde_json()

    conversor = ConversorMoneda()
    try:
        while True:
            print(f"{Colores.AZUL}\n--- 🛠️ ALPHA TECH (v4.0 MODULAR) ---{Colores.RESET}")
            print(f"{Colores.VERDE}Próximo ID automático: {sistema.proximo_id}{Colores.RESET}")
            print(f"{Colores.VERDE}1. Registrar nueva orden{Colores.RESET}")
            print(f"{Colores.VERDE}2. Ver todas las órdenes{Colores.RESET}")
            print(f"{Colores.VERDE}3. Cambiar estado de una orden{Colores.RESET}")
            print(f"{Colores.VERDE}4. Ver informe de rendimiento del taller{Colores.RESET}")
            print(f"{Colores.VERDE}5. Buscar orden por ID{Colores.RESET}")
            print(f"{Colores.VERDE}6. Conversor de Moneda{Colores.RESET}")
            print(f"{Colores.VERDE}7. Ver pagos de una orden{Colores.RESET}")
            print(f"{Colores.VERDE}8. Conversor de Moneda{Colores.RESET}")
            print(f"{Colores.VERDE}9. Registrar pago para una orden{Colores.RESET}")
            print(f"{Colores.VERDE}10. Ver cierre de caja del día{Colores.RESET}")
            print(f"{Colores.VERDE}11. Ver equipos retrasados{Colores.RESET}")
            print(f"{Colores.VERDE}12. Exportar reporte a TXT{Colores.RESET}")
            print(f"{Colores.VERDE}13. Verificar morosidad{Colores.RESET}")
            print(f"{Colores.VERDE}14. Guardar y Salir{Colores.RESET}")
            

            opcion = input(f"{Colores.AZUL}Seleccione (1-14): {Colores.RESET}")
        
            if opcion == "1":
                cli = input(f"{Colores.AZUL}Cliente: {Colores.RESET}").capitalize().strip()
                if not cli:
                    print(f"{Colores.ROJO}❌ [ERROR]: El nombre del cliente no puede estar vacío.{Colores.RESET}")
                    continue
                dev = input(f"{Colores.AZUL}Dispositivo: {Colores.RESET}").capitalize().strip()
                if not dev:
                    print(f"{Colores.ROJO}❌ [ERROR]: El nombre del dispositivo no puede estar vacío.{Colores.RESET}")
                    continue
                fal = input(f"{Colores.ROJO}Falla: {Colores.RESET}").capitalize().strip()
                if not fal:
                    print(f"{Colores.ROJO}❌ [ERROR]: La descripción de la falla no puede estar vacía.{Colores.RESET}")
                    continue
                try:
                    pre = float(input(f"{Colores.AZUL}Presupuesto ($): {Colores.RESET}"))
                    sistema.registrar_equipo(cli, dev, fal, pre)
                except ValueError:
                    print(f"{Colores.ROJO}❌ [ERROR]: El presupuesto debe ser un número.{Colores.RESET}")
                input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}") 
                time.sleep(1)
            
            elif opcion == "2":
                sistema.mostrar_taller_activo()
                input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
                time.sleep(1)
                input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")

            elif opcion == "3":
                print(f"{Colores.AZUL}--- Cambiar Estado de Orden ---{Colores.RESET}")
                try:
                    # Pedimos los datos
                    id_o = int(input(f"{Colores.AZUL}ID de orden a actualizar: {Colores.RESET}"))
                    opc = int(input(f"{Colores.AZUL}Estados: 1. En Reparación, 2. Reparado (listo para entregar), 3. Entregado: {Colores.RESET}"))
                    
                    # Definimos el mapeo de estados para mayor control
                    mapeo_estados = {
                        1: "En Reparación", 
                        2: "Reparado (listo para entregar)", 
                        3: "Entregado"
                    }
                    
                    if opc in mapeo_estados:
                        nuevo_est = mapeo_estados[opc]
                        
                        # Convertimos ID a string y ejecutamos la modificación
                        if sistema.modificar_estado_equipo(str(id_o), nuevo_est):
                            print(f"{Colores.VERDE}🔄 Estado actualizado a: {nuevo_est}.{Colores.RESET}")
                        else:
                            print(f"{Colores.ROJO}❌ Orden no encontrada.{Colores.RESET}")
                    else:
                        print(f"{Colores.ROJO}❌ [ERROR]: Opción de estado no válida.{Colores.RESET}")
                        
                except ValueError:
                    print(f"{Colores.ROJO}❌ [ERROR]: El ID y la opción de estado deben ser números.{Colores.RESET}")
                
                time.sleep(1)
                input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")

            elif opcion == "4":
                sistema.generar_reporte_rendimiento()
                time.sleep(3)  # Pausa para que el usuario pueda leer el informe
                input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
            elif opcion=="5":
                try:
                    id_orden = int(input(f"{Colores.AZUL}ID de orden a buscar: {Colores.RESET}"))
                except ValueError:
                    print(f"{Colores.ROJO}❌ [ERROR]: El ID de orden debe ser un número.{Colores.RESET}")
                    continue
                id_orden=str(id_orden)  # Convertimos a string para la búsqueda 
                orden = sistema.buscar_orden(id_orden)
                if orden:
            
                    print(f"{Colores.AZUL}🔍 Orden encontrada: {orden.obtener_id()}, Clinte: {orden.obtener_cliente()}, Dispositivo: {orden.obtener_dispositivo()}, Falla: {orden.obtener_falla()}{Colores.RESET}")
                else:
                    print(f"{Colores.ROJO}❌ Orden no encontrada.{Colores.RESET}")
                time.sleep(1)
                input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
            elif opcion == "6":
                try:
                    montousd = float(input(f"{Colores.AZUL}Ingrese el monto en USD que desea dar su equivalente: {Colores.RESET}"))
                    conversor = ConversorMoneda()
                    conversor.imprimir_tasas_equivalentes(montousd)
                except ValueError:
                    print(f"{Colores.ROJO}❌ [ERROR]: El monto en USD debe ser un número.{Colores.RESET}")
                time.sleep(1)
                input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
            elif opcion == "7":
                try:
                    idbuscar = int(input(f"{Colores.AZUL}Ingrese el ID de la orden a para ver sus pagos: {Colores.RESET}"))
                except ValueError:
                    print(f"{Colores.ROJO}❌ [ERROR]: El ID de orden debe ser un número.{Colores.RESET}")
                idbuscar=str(idbuscar)  # Convertimos a string para la búsqueda
                sistema.ver_pagos(idbuscar)
                time.sleep(1)
                input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
            elif opcion == "8":
                entrada = input(f"{Colores.AZUL}Introduzca el nombre a buscar: {Colores.RESET}").strip()
            
                # Validamos: quitamos los espacios para comprobar solo las letras
                # .replace(" ", "") permite que "Juan Perez" sea válido pero "Juan123" no.
                if not entrada or not entrada.replace(" ", "").isalpha():
                    print(f"{Colores.ROJO}❌ [ERROR]: Nombre inválido. Solo se permiten letras y espacios.{Colores.RESET}")
                    input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
                    continue
            
                # Si pasa la validación, buscamos
                encontrados = sistema.buscar_orden_por_nombre(entrada)
            
            
                if encontrados:
                    print(f"{Colores.VERDE}\n✅ Se encontraron {len(encontrados)} resultados:")
                    for equipo in encontrados:
                        print(f"🆔 #{equipo.obtener_id()} | 👤 {equipo.obtener_cliente()}")
                else:
                    print(f"{Colores.ROJO}❌ No se encontraron resultados.{Colores.RESET}")
                input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
                time.sleep(1)
                print(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
            elif opcion == "9":
                try:
                    id_pago = int(input(f"{Colores.AZUL}Ingrese el ID de la orden: {Colores.RESET}"))
                    id_pago = str(id_pago)
                
                    # Pedimos los datos faltantes para el pago
                    monto = float(input(f"{Colores.AZUL}Monto a registrar: {Colores.RESET}"))
                    moneda = input(f"{Colores.AZUL}Moneda (USD/BS): {Colores.RESET}").upper()
                
                # Ahora sí pasamos los 3 argumentos que tu función necesita
                    if sistema.registrar_pago(id_pago, monto, moneda):
                        print(f"{Colores.VERDE}✅ Pago registrado correctamente.{Colores.RESET}")
                    else:
                        print(f"{Colores.ROJO}❌ No se pudo registrar el pago.{Colores.RESET}")
                    
                except ValueError:
                    print(f"{Colores.ROJO}❌ [ERROR]: El ID y el monto deben ser numéricos.{Colores.RESET}")
                input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")   
                time.sleep(1)
            elif opcion == "10":
                sistema.generar_cierre_caja()
                input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
            elif opcion == "11":
                sistema.mostrar_equipos_retrasados()
                input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
            elif opcion == "12":
                sistema.exportar_reporte_txt()
                input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
            elif opcion == "13":
                sistema.verificar_morosidad()
                input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
            elif opcion == "14":
                sistema.guardar_en_json()
                print(f"\n{Colores.AMARILLO}⚠️ Cerrando el sistema...{Colores.RESET}")
                sistema.generar_cierre_caja() # Ejecuta el reporte automáticamente
                print(f"{Colores.VERDE}💾 ¡Hasta mañana!{Colores.RESET}")
                break
            else:
                print(f"{Colores.AMARILLO}⚠️ Opción no válida.{Colores.RESET}")
            time.sleep(1)
            input(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
    except Exception as e:
        # Si ocurre cualquier error, el programa te avisa qué pasó en lugar de cerrarse
        print(f"\n{Colores.ROJO}❌ [ERROR CRÍTICO]: Ocurrió un problema inesperado: {e}{Colores.RESET}")
        
    finally:
        # ESTO SE EJECUTA SIEMPRE, ya sea que el usuario salió bien o hubo un error
        print("\n⚠️ Guardando sistema de forma segura...")
        sistema.guardar_en_json()
        sistema.crear_backup() 
        sistema.generar_cierre_caja()
        print("👋 ¡Hasta mañana!")        

if __name__ == "__main__":
    ejecutar_menu()