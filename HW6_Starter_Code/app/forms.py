from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class CustomerForm(Form):
	first_name = StringField('first_name', validators=[DataRequired()])
	last_name = StringField('last_name', validators=[DataRequired()])
    company = StringField('company', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired()])

    #add Additional address fields here

class OrderForm(Form):
    name_of_part = StringField('name_of_part', validators=[DataRequired])
    manufacturer_of_part = StringField('manufacturer_of_part', validators=[DataRequired])


