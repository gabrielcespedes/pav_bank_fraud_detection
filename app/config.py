import os # manejar variables de entorno
from dotenv import load_dotenv # para cargar el archivo .env

# cargar variables de entorno desde .env
load_dotenv()

# BASE_DIR apunta a la carpeta 'app'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Ruta a la carpeta 'instance' dentro de 'app'
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')

# Ruta absoluta al archivo usuarios.db dentro de 'app/instance'
DB_PATH = os.path.join(INSTANCE_DIR, 'usuarios.db')

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024 # 10MB
    SQLALCHEMY_DATABASE_URI = "sqlite:///usuarios.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
