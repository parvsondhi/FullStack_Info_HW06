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

class AddressForm(Form):
    # Add additional Address fields here
    street_address = StringField('street_address', render_kw={'class': 'form-control', 'placeholder': '1378 Sesame Street', 'required': True}, validators=[DataRequired('Please a street address.')])
    city = StringField('city', render_kw={'class': 'form-control', 'placeholder': 'Berkeley', 'required': True}, validators=[DataRequired('Please the city.')])
    zip_code = StringField('zip_code', render_kw={'class': 'form-control', 'placeholder': '94705', 'required': True}, validators=[DataRequired('Please the zip code.')])
    state = StringField('state', render_kw={'class': 'form-control', 'placeholder': 'CA'}, validators=[])
    country = StringField('country', render_kw={'class': 'form-control', 'placeholder': 'United States of America'}, validators=[])

class OrderForm(Form):
    # Add order input form fields here
    name_of_part = StringField('name_of_part', render_kw={'class': 'form-control', 'placeholder': 'Hydraulic Phallic Pressure Pump', 'required': True}, validators=[DataRequired('Please enter the name of the requested part.')])
    manufacturer_of_part = StringField('manufacturer_of_part', render_kw={'class': 'form-control', 'placeholder': 'S3 Xtreme Ltd', 'required': True}, validators=[DataRequired('Please enter the manufacturer.')])
