from werkzeug.security import check_password_hash
from app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(250))

    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'{self.full_name}'
