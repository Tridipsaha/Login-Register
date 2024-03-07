from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, RadioField, SubmitField
from wtforms.validators import Email, EqualTo, DataRequired, Length

class UserForm(FlaskForm):
    name = StringField(label="Username:", validators=[DataRequired(), Length(min=4, max=15)])
    e_mail = EmailField(label="Email Address:", validators=[DataRequired(), Email()])
    phone = StringField(label="Phone number:", validators=[DataRequired()])  # Use StringField
    pasw = PasswordField(label="Password:", validators=[DataRequired(), Length(min=8)])
    cnfm_pasw = PasswordField(label="Confirm Password:", validators=[DataRequired(), EqualTo('pasw')])
    gender = RadioField(label="Gender", choices=['Male', 'Female'], validators=[DataRequired()])
    submit = SubmitField(label='Submit')
