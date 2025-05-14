from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    user_name = db.Column(db.String(1000),unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    sdt = db.Column(db.String(100))
