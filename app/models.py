from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import  generate_password_hash

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    correo = db.Column(db.String(120), unique = True, nullable = False)
    usuario = db.Column(db.String(80), unique = True, nullable = False)
    password_hash = db.Column(db.String(128), nullable = False)

    def __init__(self, nombre, correo, usuario, password):
        self.nombre = nombre
        self.correo = correo
        self.usuario = usuario
        self.password_hash =  generate_password_hash(password) 