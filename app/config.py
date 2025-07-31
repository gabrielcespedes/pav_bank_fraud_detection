import os # manejar variables de entorno
from dotenv import load_dotenv # para cargar el archivo .env

# cargar variables de entorno desde .env
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024 # 10MB
    SQLALCHEMY_DATABASE_URI = "sqlite:///usuarios.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
