import json

class ConversorMoneda:
    def __init__(self, archivo_config="config.json"):
        self.archivo_config = archivo_config
        self.tasa_bcv = self.cargar_tasa()

    def cargar_tasa(self):
        try:
            with open(self.archivo_config, "r") as f:
                datos = json.load(f)
                return datos.get("tasa_bcv", 600.50) # Valor por defecto si no encuentra el archivo
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ No se encontró config.json, usando tasa por defecto.")
            return 600.50

    def convertir_usd_a_bs(self, monto_usd):
        return monto_usd * self.tasa_bcv