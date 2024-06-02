from flask import Flask
from .controller.books_controller import books
from .config import dbUrl
from .service.connectDB import ConnectDB
from .util.phobert_model import Phobert
def create_app():
    app = Flask(__name__)
    ConnectDB.get_instance(dbUrl)
    Phobert.get_instance()
    app.register_blueprint(books)
    return app
