from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError
from fold.model import User

class RegisterForm(FlaskForm):
    def validate_username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists')

    def validate_email(self,email_to_check):
        email=User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('email already registered')


    username=StringField(label="Username: ",validators=[Length(min=2,max=30),DataRequired()])
    email=StringField(label="Email: ")
    password1=PasswordField(label="Enter Password",validators=[Length(min=6),DataRequired()])
    password2=PasswordField(label="Confirm Password",validators=[EqualTo('password1'),DataRequired()])
    submit=SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    username=StringField(label='User Name: ',validators=[DataRequired()])
    password=PasswordField(label='Password ',validators=[DataRequired()])
    submit=SubmitField(label="Sign In")

class ContactForm(FlaskForm):
    name=StringField(label='Name: ',validators=[DataRequired()])
    phone_no=StringField(label='Phone No: ')
    email=StringField(label="Email: ")
    submit=SubmitField(label="Add Contact")

