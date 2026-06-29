from conversor import ConversorMoneda
def imprimir_tasas_equivalentes(monto_usd):
        # Aseguramos que sea float
        monto_usd = float(monto_usd)
        
        # Calculamos cuánto es el monto en cada moneda
        val_bcv  = monto_usd * 630.00
        val_euro = monto_usd * 710.00
        val_usdt = monto_usd * 795.00
        
        print(f"\n{'='*40}")
        print(f"💰 PRECIO BASE: ${monto_usd:.2f} USD")
        print(f"{'='*40}")
        print(f"{'Tasa de Cambio':<15} | {'Equivalente en Bs'}")
        print(f"{'-'*40}")
        print(f"{'BCV':<15} | {val_bcv:>15,.2f} Bs")
        print(f"{'EURO':<15} | {val_euro:>15,.2f} Bs")
        print(f"{'USDT':<15} | {val_usdt:>15,.2f} Bs")
        print(f"{'='*40}")
        
#prueba 
imprimir_tasas_equivalentes(100)  # Ejemplo con 100 USD