from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from oauthlib.oauth2 import WebApplicationClient

# Configuration


app = Flask(__name__)
app.config['SECRET_KEY'] = '17176e02a219512af8df10664e155a71'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = u"Please Login to continue"
login_manager.login_message_category = "info"
from app import routes
