from fold import db, login_manager
from fold import app
from fold import bcrpyt
from flask_login import UserMixin

from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(length=30),nullable=False,unique=True)
    email=db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash=db.Column(db.String(length=60),nullable=False)
    items=db.relationship('Item',backref='owned_user',lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plain_text_password):
        self.password_hash=bcrpyt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self,attempted_password):
        return bcrpyt.check_password_hash(self.password_hash, attempted_password)




class Item(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),nullable=False,unique=True)
    phone_no=db.Column(db.String(length=15),nullable=False)
    email=db.Column(db.String(length=30),nullable=False)
    owner=db.Column(db.Integer(),db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Item{self.name}"