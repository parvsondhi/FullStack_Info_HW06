from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, OrderForm, AddressForm
# Access the models file to use SQL functions
from .models import *


@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    customerForm = CustomerForm()
    addressForm = AddressForm()
    if customerForm.validate_on_submit():
        # Get data from the form
        first_name = customerForm.first_name.data
        last_name = customerForm.last_name.data
        company = customerForm.company.data
        email = customerForm.email.data
        phone = customerForm.phone.data

        street_address = addressForm.street_address.data
        city = addressForm.city.data
        state = addressForm.state.data
        country = addressForm.country.data
        zip_code = addressForm.zip_code.data

        # Send data from form to Database
        customer_id = insert_data(first_name, last_name, company, email, phone)
        insert_address(street_address, city, state, country, zip_code, customer_id)
        return redirect('/customers')
    return render_template('customer.html', customerForm=customerForm, addressForm=addressForm)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()
    orders = retrieve_orders()
    return render_template('home.html', customers=customers, orders=orders)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    form = OrderForm()
    if form.validate_on_submit():
        # Get data from the form
        name_of_part = form.name_of_part.data
        manufacturer_of_part = form.manufacturer_of_part.data
        order_id = insert_order(name_of_part, manufacturer_of_part, value)
        # Send data from form to Database
        insert_customer_order(value, order_id)
        return redirect('/customers')
    return render_template('order.html', form=form)
