from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
lista_usuarios = ["Márcio", "Felipe", "Matheus", "Alexandre", "Sandra"]
app.config["SECRET_KEY"] = 'd25ad6e2701f3459a5898f5896e3b891'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "alert-info"


from comunidadeImpressonadora import routes
