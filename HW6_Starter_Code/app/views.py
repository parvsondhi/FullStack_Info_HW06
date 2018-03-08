from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm
from .forms import OrderForm
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
        firstname = form.firstname.data
        lastname = form.lastname.data
        company = form.company.data
        email = form.email.data
        phone = form.phone.data
        address = form.address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zipcode = form.zipcode.data

        # Send data from form to Database
        customer_id = insert_customer(firstname,lastname,company,email,phone)
        insert_address(address,city,state,country,zipcode,customer_id)
        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()
    orders = retrieve_orders()
    return render_template('home.html',
                            customers=customers,
                            orders=orders)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    form = OrderForm()
    if form.validate_on_submit():
        # Get data from the form
        name_of_part = form.name_of_part.data
        manufacturer = form.manufacturer.data

        # Send data from form to Database
        order_id = insert_order(name_of_part, manufacturer, value)
        insert_customers_order(value, order_id)
        return redirect('/customers')
    return render_template('order.html', form=form)
