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

from flaskapp import routes
