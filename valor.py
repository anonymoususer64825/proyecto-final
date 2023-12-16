import pandas as pd

# Rutas al archivo de rutas y usuarios
archivo_rutas = 'rutas_con_costos_y_precios.csv'
archivo_usuarios = 'usuarios_y_rutas_preferidas_con_faker.csv'

# Leer los archivos CSV
df_rutas = pd.read_csv(archivo_rutas)
df_usuarios = pd.read_csv(archivo_usuarios)

# Inicializar columnas para los ingresos esperados y la ganancia neta
df_rutas['Ingresos Esperados'] = 0
df_rutas['Ganancia Neta'] = 0

# Calcular los ingresos esperados y la ganancia neta para cada ruta
for ruta_id in df_rutas['ID Ruta']:
    # Contar cuántas veces aparece cada ruta en las preferencias de los usuarios
    total_usuarios = sum(
        (df_usuarios['Ruta Preferida 1'] == ruta_id) |
        (df_usuarios['Ruta Preferida 2'] == ruta_id) |
        (df_usuarios['Ruta Preferida 3'] == ruta_id)
    )

    # Calcular los ingresos esperados
    precio_ticket = df_rutas.loc[df_rutas['ID Ruta'] == ruta_id, 'Precio por Ticket'].iloc[0]
    ingresos = total_usuarios * precio_ticket
    df_rutas.loc[df_rutas['ID Ruta'] == ruta_id, 'Ingresos Esperados'] = ingresos

    # Calcular la ganancia neta (ingresos - costo operativo)
    costo_operativo = df_rutas.loc[df_rutas['ID Ruta'] == ruta_id, 'Costo Operativo'].iloc[0]
    df_rutas.loc[df_rutas['ID Ruta'] == ruta_id, 'Ganancia Neta'] = ingresos - costo_operativo

# Guardar los resultados en un nuevo archivo CSV
archivo_resultados = 'rutas_con_ingresos_y_ganancias_netas.csv'
df_rutas.to_csv(archivo_resultados, index=False, encoding='utf-8-sig')

print("Archivo generado:", archivo_resultados)
