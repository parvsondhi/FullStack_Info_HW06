from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, AddressForm
# Access the models file to use SQL functions
from .models import *


@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    Addform = AddressForm()
    if form.validate_on_submit():
        # Get data from the form
        company = form.company.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone = form.phone.data
        # Send data from form to Database
        insert_customer(company,email,first_name,last_name,phone)
        return redirect('/customers')
    return render_template('customer.html', form=form, Addform=Addform)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()
    print(customers)
    return render_template('home.html',
                            customers=customers)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    form = OrderForm()
    if form.validate_on_submit():
        # Get data from the form
        name_of_part = form.name_of_part.data
        manufacturer_of_part = form.manufacturer_of_part.data
        # Send data from form to Database
        insert_order(name_of_part,manufacturer_of_part)
        return redirect('/customers')
    return render_template('order.html', form=orderForm)

@app.route('/orders')
def display_order():
    # Retreive data from database to display
    orders = retrieve_orders()
    print(orders)
    return render_template('home.html',
                            orders=orders)
