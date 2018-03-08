from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, OrderForm, AddressForm
from .models import *
# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    customerForm = CustomerForm()
    addressForm = AddressForm()
    if customerForm.validate_on_submit() and addressForm.validate_on_submit():

        company = customerForm.company.data
        first_name = customerForm.first_name.data
        last_name = customerForm.last_name.data
        email = customerForm.email.data
        phone = customerForm.phone.data

        street_address = addressForm.street_address.data
        city = addressForm.city.data
        state = addressForm.state.data
        country = addressForm.country.data
        zip_code = addressForm.zip_code.data
        # Get data from the form
        # Send data from form to Database

        customer_id = insert_customerData(company, email, first_name, last_name, phone)
        insert_addressData(street_address, city, state, country, zip_code, customer_id)
        return redirect('/customers')
    return render_template('customer.html', customerForm=customerForm, addressForm=addressForm)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()
    orders = retrieve_orders()
    return render_template('home.html',
                            customers=customers, orders=orders)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    orderForm = OrderForm()
    if orderForm.validate_on_submit():
        part = orderForm.name_of_part.data
        manufacturer = orderForm.manufacturer_of_part.data
        order_id = insert_orderData(part, manufacturer, value)
        insert_customerOrderData(value, order_id)
        # Get data from the form
        # Send data from form to Database
        return redirect('/customers')
    return render_template('order.html', form=orderForm)
