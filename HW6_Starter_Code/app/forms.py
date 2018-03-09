from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
# from wtforms_components import PhoneNumberField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class CustomerForm(Form):
	firstName = StringField('firstName', validators=[DataRequired()])
	lastName = StringField('lastName', validators=[DataRequired()])
	company = StringField('company', validators=[DataRequired()])
	email = EmailField('email', validators=[DataRequired()])
	telephone = StringField('telephone', validators=[DataRequired()])

	# Add additional Address fields here
	streetAddress = StringField('streetAddress', validators=[DataRequired()])
	state = StringField('state', validators=[DataRequired()])
	country = StringField('country', validators=[DataRequired()])
	zipCode = StringField('zipCode', validators=[DataRequired()])


class orderForm(Form):
	# Add order input form fields here
	nameOfPart = StringField('nameOfPart', validators=[DataRequired()])
	manufacturerOfPart = StringField('manufacturerOfPart', validators=[DataRequired()])
	