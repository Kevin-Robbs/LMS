from flaskApp import db
from flaskApp import bcrypt

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(36), primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(100), nullable=False)
    role_id = db.Column(db.String(36), db.ForeignKey('roles.id'), nullable=False)
    account_status = db.Column(db.Enum('active', 'inactive', 'suspended'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, id, first_name, last_name, email, password, phone_number, role_id, created_at, updated_at):
        print(self)
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.role_id = role_id
        self.created_at = created_at
        self.updated_at = updated_at
        
    def validatePassword(self, password):
        return bcrypt.check_password_hash(self.password, password)
