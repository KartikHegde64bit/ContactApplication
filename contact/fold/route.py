from fold import app
from flask import render_template, redirect, url_for, flash,request,jsonify
from fold.model import Item
from fold.model import User
from fold.forms import LoginForm,RegisterForm
from flask_login import login_user
from fold import db
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy(app)


contact_storage={}

usernamee=''

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/contact')
def contact_page():
    items = Item.query.all()
    return render_template('contact_info.html',items=items)

@app.route('/register',methods=['GET','POST'])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create=User(username=form.username.data,email=form.email.data,password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        usernamee=form.username.data
        return redirect(url_for('contact_page'))
    
    if form.errors!={}:
        for err_msg in form.errors.values():
            flash(f'there was an error :{err_msg}',category='danger')
    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login_page():
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user=User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success logged in as:{attempted_user.username}')
            return redirect(url_for('contact_page'))
        else:
            flash('Username or password incorrect! try again',category='danger')


    return render_template('login.html',form=form)

@app.route('/contact', methods=['GET','POST'])
def getvalue():
    name=request.form['name']
    phone=request.form['phone_no']
    email=request.form['email']
    contact_storage[usernamee]={name:[phone,email]}
    return render_template('contact_info.html',info=contact_storage[usernamee])

