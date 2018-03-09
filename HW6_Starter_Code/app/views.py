from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, OrderForm #
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
        firstName = form.firstName.data
        lastName = form.lastName.data
        company = form.company.data
        email = form.email.data
        phone = form.phone.data
        insert_data(firstName,lastName,company,email,phone)

        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()
    orders = retrieve_orders()
    return render_template('home.html',
                            customer=customers, orders=orders)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    form = OrderForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        partName = form.partName.data
        manufacturerName = form.manufacturerName.data
        order_id = insert_order(partName, manufacturerName,value)
        insert_cus_order(value,order_id)
        return redirect('/customers')
    return render_template('order.html', form=form)

# @app.route('/orders')
# def get_order():
#     # Retreive data from database to display
#     orders = retrieve_orders()
#     return render_template('home.html',
#                             orders=orders)


