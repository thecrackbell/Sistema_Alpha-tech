import time
from lista_reparaciones import ListaReparaciones
from colores import Colores
from conversor import convertir_a_dolares, convertir_a_pesos

def ejecutar_menu():
    sistema = ListaReparaciones()
    sistema.cargar_desde_json()
    
    while True:
        print(f"{Colores.AZUL}\n--- 🛠️ ALPHA TECH (v4.0 MODULAR) ---{Colores.RESET}")
        print(f"{Colores.VERDE}Próximo ID automático: {sistema.proximo_id}{Colores.RESET}")
        print(f"{Colores.VERDE}1. Registrar nueva orden{Colores.RESET}")
        print(f"{Colores.VERDE}2. Ver todas las órdenes{Colores.RESET}")
        print(f"{Colores.VERDE}3. Cambiar estado de una orden{Colores.RESET}")
        print(f"{Colores.VERDE}4. Ver informe de rendimiento del taller{Colores.RESET}")
        print(f"{Colores.VERDE}5. Buscar orden por ID{Colores.RESET}")
        print(f"{Colores.VERDE}6. Buscar por Nombre de Cliente{Colores.RESET}")
        print(f"{Colores.VERDE}7. Guardar y Salir{Colores.RESET}")

        opcion = input(f"{Colores.AZUL}Seleccione (1-7): {Colores.RESET}")
        
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

        elif opcion == "3":
            id_o = input(f"{Colores.AZUL}ID de orden a actualizar: {Colores.RESET}")
            nuevo_est = input(f"{Colores.AZUL}Nuevo estado: {Colores.RESET}")
            if sistema.modificar_estado_equipo(id_o, nuevo_est):
                print(f"{Colores.VERDE}🔄 Estado actualizado.{Colores.RESET}")
            else:
                print(f"{Colores.ROJO}❌ Orden no encontrada.{Colores.RESET}")
            time.sleep(3)
            print(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")

        elif opcion == "4":
            sistema.generar_reporte_rendimiento()
            time.sleep(3)  # Pausa para que el usuario pueda leer el informe
            print(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
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
            time.sleep(3)
            print(f"{Colores.VERDE}Presione Enter para continuar...{Colores.RESET}")
        elif opcion == "6":
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
           
        elif opcion == "7":
            sistema.guardar_en_json()
            print(f"{Colores.VERDE}💾 ¡Hasta mañana!{Colores.RESET}")
            break
        else:
            print(f"{Colores.AMARILLO}⚠️ Opción no válida.{Colores.RESET}")

if __name__ == "__main__":
    ejecutar_menu()