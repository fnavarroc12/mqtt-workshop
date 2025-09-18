# -*- coding: utf-8 -*-
# === Generador de datos aleatorios de sensores ===
# 
# Este script simula un dispositivo IoT que envía datos. Utiliza una distribución normal (gaussiana) 
# para que la mayoría de los valores se concentren alrededor del centro del rango, pero ocasionalmente 
# se acerquen a los extremos, simulando un comportamiento más realista.

import time
import json
import random

def generar_datos_sensor(measure_id: str, valor_min: float, valor_max: float) -> float:
    """
    Genera una lectura de sensor simulada con una distribución normal.

    Args:
        measure_id: Identificador único de la métrica (ej. "temp_sala_1").
        valor_min: Valor mínimo del rango del sensor.
        valor_max: Valor máximo del rango del sensor.

    Returns:
        Un diccionario con los datos del sensor.
    """
    # Calcula el punto medio y la desviación estándar para la distribución normal
    media = (valor_max + valor_min) / 2

    # La desviación estándar se ajusta para que ~99.7% de los valores caigan dentro del rango
    desviacion_estandar = (valor_max - media) / 3 

    # Genera un valor usando una distribución normal
    valor_generado = random.gauss(media, desviacion_estandar)
    
    # Asegura que el valor se mantenga dentro de los límites definidos
    valor_final = max(valor_min, min(valor_max, valor_generado))

    return valor_final


# --- Ejemplo de uso ---
if __name__ == "__main__":
    secuencia = 0
    try:
        print("Iniciando simulación de sensor. Presiona CTRL+C para detener.")
        while True:
            
            # Simula un sensor de temperatura para una sala
            datos_temperatura = generar_datos_sensor(
                measure_id="temp_sala_1",
                valor_min=18.0,
                valor_max=26.0
            )
            print(f"Generado: {json.dumps(datos_temperatura)}")
            
            # Simula un sensor de humedad para la misma sala
            datos_humedad = generar_datos_sensor(
                measure_id="hum_sala_1",
                valor_min=40.0,
                valor_max=60.0
            )
            print(f"Generado: {json.dumps(datos_humedad)}")
            
            # Espera 5 segundos antes de la siguiente lectura
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nSimulación detenida por el usuario.")

# Fin del script
