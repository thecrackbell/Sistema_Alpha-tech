class ConversorMoneda:
    def __init__(self):
        # Aquí defines tus tasas (deberás actualizarlas manualmente o por API)
        self.tasas = {
            "bsv": 622.21,   # Tasa BCV
            "usdt": 708.39,  # Tasa USDT
            "euro": 789.25   # Tasa Euro
        }

    def calcular_en_bolivares(self, monto_usd, tipo_tasa):
        """Calcula el total en Bs basado en la tasa elegida"""
        tasa = self.tasas.get(tipo_tasa.lower())
        if tasa:
            return monto_usd * tasa
        return None