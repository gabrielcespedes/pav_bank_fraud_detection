# **Bank Fraud Detection**

Aplicación web para detectar fraudes en apertura de cuentas bancarias a partir de archivos Excel o CSV, usando modelos de Machine Learning.

## **Estructura del proyecto**

```
PAV/
│
├── app/
│ ├── ml/ # Modelos y variables de configuración (joblib, Python)
│ ├── outputs/ # Archivos generados (predicciones)
│ ├── routes/ # Rutas y lógica de Flask (Blueprints)
│ ├── static/ # Recursos estáticos (CSS, JS, imágenes)
│ ├── templates/ # Plantillas HTML (Jinja2)
│ ├── uploads/ # Archivos subidos por el usuario
│ ├── utils/ # Funciones de predicción y utilidades
│ ├── init.py # Inicialización de la aplicación Flask
│ ├── app.py # Configuración y creación de la aplicación Flask
│ ├── config.py # Configuración de la aplicación (flask.config.from_object)
│ ├── models.py # Modelos de base de datos (SQLAlchemy)
│
├── .env # Variables de entorno (local)
├── Procfile # Comando de inicio para Render (gunicorn)
├── requirements.txt # Dependencias Python
├── wsgi.py # Punto de entrada WSGI para producción
│
├── data/ # Dataset original 
├── ml/ # Proyecto ML original 
├── s3/ # Carga desde AWS S3
```

## Despliegue en Render

1. Subir el proyecto a GitHub.

2. En Render:

- Crear un Web Service desde el repo.

- Configurar Python 3.13.x en "Environment".

- Build Command: pip install -r requirements.txt

- Start Command: gunicorn -w 4 -b 0.0.0.0:10000 app.wsgi:app

- Variables de entorno desde el panel 

3. Rutas disponibles:

- / : Login

- /registro : Registro de usuarios

- /prediccion : Subir archivo y obtener predicciones.

4. Uso en local

- Crear entorno virtual

```
python -m venv .venv
source .venv/Scripts/activate # Windows
```

- Instalar dependencias

```
pip install -r requirements.txt
```

- Ejecutar localmente
```
python -m app.app
```

- Link Web (esperar a que servicio Render inicialice la aplicación): 

https://pav-bank-fraud-detection.onrender.com/

- Datos para predecir de ejemplo

https://drive.google.com/drive/folders/1db0Ap_jgSwObAg_1ev5f1sxsyKm2qOUJ?usp=sharing

## Puntos importantes

- Archivos subidos (uploads/) y generados (outputs/) son temporales en Render y se eliminan al reiniciar el deploy.

- Base de datos SQLite3 es volátil en Render. Se recomienda migrar a PostgreSQL para persistencia
