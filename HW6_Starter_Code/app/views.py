from flask import render_template, redirect, request
from app import app, models, db
from .forms import *
# Access the models file to use SQL functions
from .models import *

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
        phone = form.phone.data
        street_address = form.street_address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zipcode = form.zipcode.data
        cust_id = insert_customer(first_name, last_name, company, email, phone)
        insert_address(street_address,city,state,country,zipcode,cust_id)
        return redirect('/customers')

    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()
    orders = retrieve_customer_to_orders()
    return render_template('home.html',
                            customers=customers, orders = orders)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
        # Get data from the form
        # Send data from form to Database
        # return redirect('/customers')
    orderform = OrderForm()
    if orderform.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        name_of_part = orderform.name.data
        manufacturer_of_part = orderform.manufacturer.data
        order_id = insert_orders(name_of_part,manufacturer_of_part)
        insert_co(order_id,value)
        return redirect('/customers')

    return render_template('order.html', form=orderform)
