from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = 'd25ad6e2701f3459a5898f5896e3b891'

if os.getenv("DATABASE_URL"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "alert-info"

from comunidadeImpressonadora import models

engine = sqlalchemy.create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table("usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("Base de Dados criado com sucesso!")
else:
    print("Base de Dados já existente!")


from comunidadeImpressonadora import routes
