from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class CustomerForm(Form):
    first_name = StringField('first_name', validators=[DataRequired('Please enter your first name.')])
    last_name = StringField('last_name', validators=[DataRequired('Please enter your last name.')])
    company = StringField('company', validators=[DataRequired('Please enter your company name.')])
    email = EmailField('email', validators=[DataRequired('Please enter your email.')])
    phone = StringField('phone', validators=[])
    # Add additional Address fields here

class OrderForm(Form):
    # Add order input form fields here
    company = StringField('company', validators=[DataRequired()])