from flask import Flask

from dictionary.model import Dictionary

app = Flask(__name__)
dict = Dictionary()
dict.load_json()


def create_app():

    app.config.from_pyfile("settings.py")

    from dictionary.views import dict_app

    app.register_blueprint(dict_app)

    return app