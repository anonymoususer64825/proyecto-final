import pandas as pd

def knapsack_problem(costs, values, budget, max_items):
    """
    Implementa el problema de la mochila 0/1 con una restricción adicional en el número de items.
    
    :param costs: Lista de costos para cada ruta.
    :param values: Lista de valores (ganancias netas) para cada ruta.
    :param budget: Presupuesto total disponible.
    :param max_items: Número máximo de rutas a seleccionar.
    :return: Lista de rutas seleccionadas.
    """
    num_items = len(values)
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for w in range(1, budget + 1):
            if costs[i-1] <= w:
                dp_table[i][w] = max(values[i-1] + dp_table[i-1][w-costs[i-1]], dp_table[i-1][w])
            else:
                dp_table[i][w] = dp_table[i-1][w]

    # Reconstruir la solución
    selected_routes = []
    w = budget
    items_selected = 0
    for i in range(num_items, 0, -1):
        if dp_table[i][w] != dp_table[i-1][w] and items_selected < max_items:
            selected_routes.append(i-1)
            w -= costs[i-1]
            items_selected += 1

    return selected_routes

# Leer el archivo CSV
archivo_rutas = 'rutas_con_ingresos_y_ganancias_netas.csv'
df_rutas = pd.read_csv(archivo_rutas)

# Solicitar datos al usuario
presupuesto = int(input("Por favor, ingrese su presupuesto máximo: "))
max_rutas = int(input("Ingrese el número máximo de rutas que desea tener: "))

# Preparar datos para el algoritmo de la mochila
costos = df_rutas['Costo Operativo'].tolist()
ganancias = df_rutas['Ganancia Neta'].tolist()

# Aplicar el algoritmo de la mochila
rutas_seleccionadas = knapsack_problem(costos, ganancias, presupuesto, max_rutas)

# Mostrar resultados
print("Rutas seleccionadas:")
for indice in rutas_seleccionadas:
    ruta_seleccionada = df_rutas.iloc[indice]
    print(f"ID Ruta: {ruta_seleccionada['ID Ruta']}, Costo: {ruta_seleccionada['Costo Operativo']}, Ganancia Neta: {ruta_seleccionada['Ganancia Neta']}")
