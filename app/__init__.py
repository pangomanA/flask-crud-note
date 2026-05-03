from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    # secret key
    app.config["SECRET_KEY"] = "scylla"

    # data base config
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project_note.db"
    app.config["SQLALCHEMY_MODIFY_TRACKING"] = False

    # initialize database
    db.init_app(app)

    # register blue 
    from . import routes
    app.register_blueprint(routes.bp)
    return app

