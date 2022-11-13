from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config

def create_app():
    app = Flask(__name__) # Se crea nueva instancia de la clase Flask
    bootstrap = Bootstrap(app)
    app.config.update(**Config.config)

    return app