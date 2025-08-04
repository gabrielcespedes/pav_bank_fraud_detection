from flask import Flask
from app.routes.main import main # importando Blueprint

from app.models import db # se importa objeto SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')        
    db.init_app(app) # inicia la base de datos con la app
    app.register_blueprint(main)

    # crea las tablas si no existen
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)
