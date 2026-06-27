def imprimir_tasas_equivalentes( monto_usd):
    # Definimos las tasas actuales
    tasas = {
        "BCV": 622.21,
        "USDT": 789.25,
        "Euro": 708.39,
    }
    
    print(f"\n--- 💱 EQUIVALENCIAS PARA ${monto_usd:.2f} ---")
    for nombre, tasa in tasas.items():
        total_bs = monto_usd * tasa
        print(f" {total_bs: >10,.2f} Bs.")
    print("------------------------------------------")
    
#prueba de la función
imprimir_tasas_equivalentes(100)