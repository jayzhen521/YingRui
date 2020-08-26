from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp

class ContactMsg(FlaskForm):
    #name, email, phoneNumber, message
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    phonenumber = StringField('Phone', validators=[DataRequired(), Length(8, 20),
        Regexp('^[1-9][0-9]*$', 0, 'Phone number format error')])
    message = StringField("Message", validators=[DataRequired()])
    submit = SubmitField('SEND')