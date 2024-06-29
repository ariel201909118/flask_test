from . import db 
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    _id = db.Column(db.Integer(), autoincrement=True, unique=True, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    
    def __repr__(self):
        return f'<{self.username}>' 
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)