from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'bc8d08cddabdb4fa5b59fd339e4cdafe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)    # database object
bcrypt = Bcrypt(app)    # password hashing
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskapp import routes
