from flask import Flask
import secrets
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = secrets.token_hex()
