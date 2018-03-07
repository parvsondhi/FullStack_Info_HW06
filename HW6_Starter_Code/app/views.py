from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, OrderForm
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
        first_name = form.first_name.data
        last_name = form.last_name.data
        company = form.company.data
        email = form.email.data
        phone = form.phone.data

        street_address = form.street_address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zip_code = form.zip_code.data

        # Send data from form to Database
        customer_id = insert_customer(first_name,last_name,company,email,phone)
        insert_address(street_address,city,state,country,zip_code,customer_id)
        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()
    orders = retrieve_orders()
    return render_template('home.html',
                            customers=customers, orders=orders)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    # Get data from the form
    orderForm = OrderForm()
    if orderForm.validate_on_submit():
        name_of_part = orderForm.name_of_part.data
        manufacturer_of_part = orderForm.manufacturer_of_part.data
        order_id = insert_order(name_of_part,manufacturer_of_part,value)
    # Send data from form to Database
        insert_customer_order(value,order_id)
        return redirect('/customers')
    return render_template('order.html', form=orderForm)
