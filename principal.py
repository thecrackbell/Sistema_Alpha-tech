import json
import time 

# =====================================================================
# SISTEMA DE GESTIÓN DE ORDENES - ALPHA TECH (AUTO-INCREMENTAL)
# =====================================================================

class Equipo:
    def __init__(self, id_orden, cliente, dispositivo, falla, presupuesto_usd, estado="Recibido (En Espera)"):
        self.__id_orden = id_orden
        self.__cliente = cliente
        self.__dispositivo = dispositivo
        self.__falla = falla
        self.__presupuesto_usd = presupuesto_usd
        self.estado = estado
        self.siguiente = None 

    def obtener_id(self): return self.__id_orden
    def obtener_cliente(self): return self.__cliente
    def obtener_dispositivo(self): return self.__dispositivo
    def obtener_falla(self): return self.__falla
    def obtener_presupuesto(self): return self.__presupuesto_usd

class ListaReparaciones:
    def __init__(self):
        self.cabeza = None
        self.proximo_id = 1001

    def registrar_equipo(self, cliente, dispositivo, falla, presupuesto_usd):
        """Para clientes nuevos: asigna un ID automáticamente"""
        id_actual = str(self.proximo_id)
        self.proximo_id += 1
        
        nuevo_equipo = Equipo(id_actual, cliente, dispositivo, falla, presupuesto_usd)
        self._insertar_al_final(nuevo_equipo)
        print(f"📌 Orden #{id_actual} registrada correctamente.")
        return True

    def _insertar_al_final(self, nuevo_equipo):
        """Método interno para no repetir lógica de inserción"""
        if self.cabeza is None:
            self.cabeza = nuevo_equipo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_equipo

    def _agregar_nodo_manual(self, id_o, cli, dev, fal, pre, est):
        """Para cargar desde JSON: conserva el ID y estado original"""
        nuevo_equipo = Equipo(id_o, cli, dev, fal, pre, est)
        self._insertar_al_final(nuevo_equipo)

    def modificar_estado_equipo(self, id_orden, nuevo_estado):
        actual = self.cabeza
        while actual is not None:
            if actual.obtener_id() == id_orden:
                actual.estado = nuevo_estado
                return True
            actual = actual.siguiente
        return False

    def guardar_en_json(self, nombre_archivo="taller_datos.json"):
        datos_a_guardar = {
            "proximo_id": self.proximo_id,
            "equipos": []
        }
        actual = self.cabeza
        while actual is not None:
            datos_a_guardar["equipos"].append({
                "id_orden": actual.obtener_id(),
                "cliente": actual.obtener_cliente(),
                "dispositivo": actual.obtener_dispositivo(),
                "falla": actual.obtener_falla(),
                "presupuesto_usd": actual.obtener_presupuesto(),
                "estado": actual.estado
            })
            actual = actual.siguiente
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos_a_guardar, archivo, indent=4, ensure_ascii=False)
        print("💾 Datos y contador guardados en disco.")

    def cargar_desde_json(self, nombre_archivo="taller_datos.json"):
        """Carga blindada: Si el JSON está corrupto, inicia el sistema vacío"""
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            self.proximo_id = datos.get("proximo_id", 1001)
            self.cabeza = None
            for e in datos.get("equipos", []):
                self._agregar_nodo_manual(
                    e.get("id_orden","N/A"), e.get("cliente","Desconocido"), e.get("dispositivo","N/A"), 
                    e.get("falla","N/A"), e.get("presupuesto_usd", 0), e.get("estado","N/A")
                )
        except (FileNotFoundError, json.JSONDecodeError):
            self.proximo_id = 1001
            self.cabeza = None
    def mostrar_taller_activo(self):
        if self.cabeza is None:
            print("\n📭 Taller vacío.")
            return
        print("\n📋 LISTADO DE ÓRDENES:")
        actual = self.cabeza
        while actual is not None:
            print(f"🆔 #{actual.obtener_id()} | {actual.obtener_dispositivo()} | Estado: {actual.estado}| Cliente: {actual.obtener_cliente()} | Falla: {actual.obtener_falla()} | Presupuesto: ${actual.obtener_presupuesto():.2f}")
            actual = actual.siguiente

def ejecutar_menu():
    sistema = ListaReparaciones()
    sistema.cargar_desde_json()
    
    while True:
        print("\n--- 🛠️ ALPHA TECH (v4.0) ---")
        print(f"Próximo ID automático: {sistema.proximo_id}")
        print("1. Registrar nueva orden")
        print("2. Ver todas las órdenes")
        print("3. Cambiar estado de una orden")
        print("4. Guardar y Salir")
        
        opcion = input("Seleccione (1-4): ")
        
        if opcion == "1":
            cli = input("Cliente: ").capitalize().strip()
            if not cli:
                print("❌ [ERROR]: El nombre del cliente no puede estar vacío.")
                continue # Vuelve al inicio del menú
            dev = input("Dispositivo: ").capitalize().strip()
            if not dev:
                print("❌ [ERROR]: El nombre del dispositivo no puede estar vacío.")
                continue # Vuelve al inicio del menú
            fal = input("Falla: ").capitalize().strip()
            if not fal:
                print("❌ [ERROR]: La descripción de la falla no puede estar vacía.")
                continue # Vuelve al inicio del menú
            try:
                pre = float(input("Presupuesto ($): "))
                sistema.registrar_equipo(cli, dev, fal, pre)
            except ValueError:
                print("❌ [ERROR]: El presupuesto debe ser un número.")
            input("Presione Enter para continuar...") 
            time.sleep(3)
        elif opcion == "2":
            sistema.mostrar_taller_activo()
            time.sleep(3)
            input("Presione Enter para continuar...")

        elif opcion == "3":
            id_o = input("ID de orden a actualizar: ")
            nuevo_est = input("Nuevo estado: ")
            if sistema.modificar_estado_equipo(id_o, nuevo_est):
                print("🔄 Estado actualizado.")
            else:
                print("❌ Orden no encontrada.")
            time.sleep(3) 
        elif opcion == "4":
            sistema.guardar_en_json()
            print("💾 ¡Hasta mañana!")
            break
        
        else:
            print("⚠️ Opción no válida.")

if __name__ == "__main__":
    ejecutar_menu()