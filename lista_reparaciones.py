import json
from equipo import Equipo

class ListaReparaciones:
    def __init__(self):
        self.cabeza = None
        self.proximo_id = 1001

    def registrar_equipo(self, cliente, dispositivo, falla, presupuesto_usd):
        id_actual = str(self.proximo_id)
        self.proximo_id += 1
        nuevo_equipo = Equipo(id_actual, cliente, dispositivo, falla, presupuesto_usd)
        self._insertar_al_final(nuevo_equipo)
        print(f"📌 Orden #{id_actual} registrada correctamente.")
        return True

    def _insertar_al_final(self, nuevo_equipo):
        if self.cabeza is None:
            self.cabeza = nuevo_equipo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_equipo

    def _agregar_nodo_manual(self, id_o, cli, dev, fal, pre, est):
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
        datos_a_guardar = {"proximo_id": self.proximo_id, "equipos": []}
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
    def generar_reporte_rendimiento(self):
        """Analiza la RAM y devuelve estadísticas del taller"""
        total_ingresos = 0.0
        conteo_estados = {}
        actual = self.cabeza
        
        while actual is not None:
            # 1. Sumar presupuesto
            total_ingresos += actual.obtener_presupuesto()
            
            # 2. Contar estados
            estado = actual.estado
            conteo_estados[estado] = conteo_estados.get(estado, 0) + 1
            
            actual = actual.siguiente
            
        print("\n📊 --- REPORTE DE RENDIMIENTO ALPHA TECH ---")
        print(f"💰 Ingreso total proyectado: ${total_ingresos:.2f}")
        print("📈 Estado de las órdenes:")
        for estado, cantidad in conteo_estados.items():
            print(f"   - {estado}: {cantidad}")
        print("============================================")
    def buscar_orden(self, id_orden):
        """Busca una orden por su ID y devuelve el objeto Equipo si se encuentra, o None si no."""
        actual = self.cabeza
        while actual is not None:
            if actual.obtener_id() == id_orden:
                return actual
            actual = actual.siguiente
        return None
    def buscar_orden_por_nombre(self, nombre_buscado):
        """Busca órdenes que coincidan con el nombre o inicial del cliente"""
        resultados = []
        nombre_buscado = nombre_buscado.lower().strip()
        actual = self.cabeza
        
        while actual is not None:
            nombre_cliente = actual.obtener_cliente().lower()
            # Verificamos si el nombre empieza con lo que buscamos o contiene el texto
            if nombre_cliente.startswith(nombre_buscado) or nombre_buscado in nombre_cliente:
                resultados.append(actual)
            actual = actual.siguiente
        
        return resultados