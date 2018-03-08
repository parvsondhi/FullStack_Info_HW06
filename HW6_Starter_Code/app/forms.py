from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class CustomerForm(Form):
	firstname = StringField('firstname', validators=[DataRequired()])
	lastname = StringField('lastname', validators=[DataRequired()])
	company = StringField('company', validators=[DataRequired()])
	email = EmailField('email', validators=[DataRequired()])
	phone = IntegerField('phone', validators=[DataRequired()])
	address = StringField('address', validators=[DataRequired()])
	city = StringField('city', validators=[DataRequired()])
	state = StringField('state', validators=[DataRequired()])
	country = StringField('country', validators=[DataRequired()])
	zipcode = IntegerField('zipcode', validators=[DataRequired()])

class OrderForm(Form):
	name_of_part = StringField('name_of_part', validators=[DataRequired()])
	manufacturer = StringField('manufacturer', validators=[DataRequired()])
