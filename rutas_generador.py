import pandas as pd
import random

# Definición de la cantidad de rutas
num_rutas = 100

# Generar datos para las rutas con valores enteros
rutas_data = {
    'ID Ruta': range(1, num_rutas + 1),
    'Costo Operativo': [random.randint(100, 500) for _ in range(num_rutas)],  # Costos operativos enteros
    'Precio por Ticket': [random.randint(10, 50) for _ in range(num_rutas)]  # Precios por ticket enteros
}

# Crear DataFrame para las rutas
df_rutas = pd.DataFrame(rutas_data)

# Guardar el DataFrame en un archivo CSV
csv_filename_rutas = 'rutas_con_costos_y_precios.csv'
df_rutas.to_csv(csv_filename_rutas, index=False, encoding='utf-8-sig')
