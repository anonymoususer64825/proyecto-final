# Optimizador de Rutas de Transporte

Este proyecto es una aplicación web que utiliza el algoritmo de la mochila para optimizar las rutas de transporte basándose en un presupuesto y una cantidad máxima de rutas. La aplicación permite a los usuarios ingresar su presupuesto y el número máximo de rutas que desean operar, y luego calcula las rutas más óptimas utilizando datos de costos operativos y ganancias netas.

## Características

- **Generador de Usuarios y Rutas:** La aplicación incluye scripts para generar datos ficticios de usuarios y sus rutas preferidas, así como las rutas con sus costos operativos y precios por ticket.
- **Interfaz de Usuario Web:** Una interfaz sencilla pero efectiva para ingresar el presupuesto y el número máximo de rutas, y para visualizar los resultados del algoritmo de la mochila.

## Tecnologías Utilizadas

- Python
- Flask
- HTML
- CSS
- JavaScript

## Dependencias

- Flask: Un micro framework web para Python.
- Flask-CORS: Una extensión de Flask para manejar el intercambio de recursos de origen cruzado (CORS).
- Pandas: Una biblioteca de Python para manipulación y análisis de datos.

## Instalación

Para ejecutar este proyecto localmente, sigue estos pasos:

1. Clona el repositorio a tu máquina local:
git clone https://github.com/tu-usuario/tu-repositorio.git

2. Navega al directorio del proyecto:
cd tu-repositorio

3. Instala las dependencias necesarias:
pip install flask
pip install flask-cors
pip install pandas

5. Ejecuta la aplicación Flask:
python app.py

## Uso

Una vez que la aplicación esté ejecutándose, abre tu navegador y ve a `http://127.0.0.1:5000/`. Deberías ver la interfaz de usuario del optimizador de rutas.

Introduce tu presupuesto máximo y el número máximo de rutas que deseas operar. Haz clic en "Calcular Rutas Óptimas" para ver los resultados.

