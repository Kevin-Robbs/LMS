from flaskApp import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, id, name, created_at, updated_at):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at