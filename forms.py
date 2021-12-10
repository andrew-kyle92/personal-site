from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, URL, Email, EqualTo, Length
from flask_ckeditor import CKEditorField


class ContactForm(FlaskForm):
    name = StringField("Full name", validators=[DataRequired()])
    email = EmailField("Email address", validators=[DataRequired(), Email("Email is not valid.")])
    phone = StringField("Phone number")
    message = CKEditorField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")
