from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class CustomerForm(Form):
	firstName = StringField('firstName', validators=[DataRequired()])
	lastName = StringField('lastNameName', validators=[DataRequired()])
	company = StringField('company', validators=[DataRequired()])
	email = EmailField('email', validators=[DataRequired()])
	phone = IntegerField('phone', validators=[DataRequired()])
    # Add additional Address fields here
	street_address = StringField('street_address', validators=[DataRequired()])
	city = StringField('firstName', validators=[DataRequired()])
	state = StringField('firstName', validators=[DataRequired()])
	country = StringField('firstName', validators=[DataRequired()])
	zip_code = IntegerField('zip_code', validators=[DataRequired()])

class OrderForm(Form):
#     # Add order input form fields here
	partName = StringField('partName', validators=[DataRequired()])
	manufacturerName = StringField('manufacturerName', validators=[DataRequired()])