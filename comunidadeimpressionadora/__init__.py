import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b508aac3d4bbe127a0bd8cd0d16bfdd7'

if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    basedir = os.path.abspath(os.path.dirname(__file__))
    sqlite_path = os.path.join(basedir, "comunidade.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{sqlite_path}"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import modules

with app.app_context():
    database.create_all()

from comunidadeimpressionadora import routes
