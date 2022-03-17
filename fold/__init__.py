
# to make the folder as package


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///contact.db'
app.config['SECRET_KEY']='eb3cb46c322809f1f80be809'
db=SQLAlchemy(app)
bcrpyt=Bcrypt(app)
login_manager=LoginManager(app)
from fold import route