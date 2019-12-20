from flask_wtf import FlaskForm, form
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, SelectMultipleField, RadioField, SelectField
from wtforms.fields.html5 import EmailField, DateField, IntegerField
from wtforms.validators import InputRequired, Email, Length, Regexp, ValidationError, NumberRange, DataRequired
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

class ContactForm(FlaskForm):
    username = StringField('Name', validators=[InputRequired()])
    email = StringField('Email',
     validators=[InputRequired(), Regexp("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", message="Must be a valid email")])
    messages = TextField('Message',
                        validators=[InputRequired(), Length(min=5, max=100, message="Your message must be between 5 to 100 characters")])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField("username",
                        validators=[InputRequired()])
    password = PasswordField("password",
                             validators=[InputRequired()])
    submit = SubmitField("Login")
