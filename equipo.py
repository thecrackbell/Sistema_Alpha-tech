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