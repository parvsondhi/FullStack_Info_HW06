from flask import render_template, redirect, request
from app import app, models, db
from .forms import *
from .models import *
# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        first_name = form.first_name.data
        last_name = form.last_name.data
        company = form.company.data
        email = form.email.data
        phone_number = form.phone_number.data
        street_address = form.street_address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zipcode = form.zipcode.data

        customer_id = insert_customer(first_name, last_name, company, email, phone_number)
        # print("Hi:" + customer_id)
        insert_address(street_address, city, state, country, zipcode, customer_id)
        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()
    orders = retrieve_orders()
    return render_template('home.html',
                            customers=customers)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
        # Get data from the form
        # Send data from form to Database
    orderform = OrderForm()
    # print (" in this function")
    # print (value)
    if orderform.validate_on_submit():
        # print ("hello")
        # print (value)
        models.insert_order(
        orderform.name_of_part.data, orderform.manufacturer_of_part.data, value
        )
        return redirect('/customers')
    return render_template('order.html', form=orderform)
