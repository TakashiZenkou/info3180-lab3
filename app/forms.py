from tkinter import Widget
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
    name  = StringField('Please enter your full name.',validators=[DataRequired()])
    email = StringField('Please enter your e-mail address.',validators=[DataRequired(), Email()])
    subject = StringField('Please enter the subject for your message.',validators=[DataRequired()])
    message = TextAreaField('Please enter the message you would like to send.',validators=[DataRequired()], widget=TextArea())