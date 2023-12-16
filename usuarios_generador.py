from faker import Faker
import pandas as pd
import random

# Inicializar Faker
fake = Faker()

# Cantidad de usuarios y rutas posibles
num_usuarios = 1000
num_rutas = 100

# Generar datos para los usuarios
data_usuarios = {
    'ID Usuario': range(1, num_usuarios + 1),
    'Nombre': [fake.first_name() for _ in range(num_usuarios)],
    'Apellido': [fake.last_name() for _ in range(num_usuarios)],
    'Ruta Preferida 1': [random.randint(1, num_rutas) for _ in range(num_usuarios)],
    'Ruta Preferida 2': [random.randint(1, num_rutas) for _ in range(num_usuarios)],
    'Ruta Preferida 3': [random.randint(1, num_rutas) for _ in range(num_usuarios)]
}

# Crear un DataFrame de pandas y guardar en un archivo CSV
df_usuarios = pd.DataFrame(data_usuarios)
csv_filename_usuarios = 'usuarios_y_rutas_preferidas_con_faker.csv'
df_usuarios.to_csv(csv_filename_usuarios, index=False, encoding='utf-8-sig')
