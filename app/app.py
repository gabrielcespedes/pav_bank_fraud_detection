from flask import Flask
from routes.main import main # importando Blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(main)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)
