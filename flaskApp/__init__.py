from flask import Flask
from flask_bcrypt import Bcrypt
import os, secrets
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@localhost:3306/{os.getenv("DB")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from flaskApp.models.user import User
from flaskApp.models.role import Role

Migrate(app, db)
app.secret_key = os.getenv('SECRET_KEY')
