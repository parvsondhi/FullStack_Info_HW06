from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired


class CustomerForm(Form):
    first_name = StringField('first_name', render_kw={'class': 'form-control', 'placeholder': 'John', 'required': True}, validators=[DataRequired('Please enter your first name.')])
    last_name = StringField('last_name', render_kw={'class': 'form-control', 'placeholder': 'Doe', 'required': True}, validators=[DataRequired('Please enter your last name.')])
    company = StringField('company', render_kw={'class': 'form-control', 'placeholder': 'Web Wizards Ltd', 'required': True}, validators=[DataRequired('Please enter your company name.')])
    email = EmailField('email', render_kw={'class': 'form-control', 'placeholder': 'j.doe@gmail.com', 'required': True}, validators=[DataRequired('Please enter your email.')])
    phone = StringField('phone', render_kw={'class': 'form-control', 'placeholder': '+1 123 346 7890'}, validators=[])

class Address(Form):
    # Add additional Address fields here
    email = StringField('street_address', validators=[DataRequired('Please a street address.')])
    city = StringField('city', validators=[DataRequired('Please the city.')])
    zip_code = StringField('zip_code', validators=[DataRequired('Please the zip code.')])
    state = StringField('state', validators=[])
    country = StringField('country', validators=[])

class OrderForm(Form):
    # Add order input form fields here
    company = StringField('company', validators=[DataRequired()])