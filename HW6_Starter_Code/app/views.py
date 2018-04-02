from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, OrderForm
from .models import *

@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    print("create_customer here")
    form = CustomerForm()
    if form.validate_on_submit():
        print('validated')
        # Get data from the form
        data = {}
        data['company'] = form.company.data
        data['email'] = form.email.data
        data['first_name'] = form.first_name.data
        data['last_name' ] = form.last_name.data
        data['phone'] = form.phone.data
        customer_id = insert_data('customers', data)
        data = {}
        data['customer_id'] = customer_id
        data['country'] = form.country.data
        data['state'] = form.state.data
        data['city'] = form.city.data
        data['street_address'] = form.street_address.data
        data['zip_code'] = form.zip_code.data
        # Send data from form to Database
        print('printing address data:')
        print(data)
        insert_data('address', data)
        return redirect('/customers')
    print('not validated')
    print(form.errors)
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    # Retrieve data from database to display   
    customers = retrieve_data('cust_address')
    print(str(customers))
    orders = retrieve_data('orders')
    return render_template(
        'home.html',
        customers=customers,
        orders=orders
        )

#@app.route('/create_order/<value>', methods=['GET', 'POST'])
@app.route('/create_order', methods=['GET', 'POST'])
def create_order():
    # Get data from the form
    form = OrderForm();
    if form.validate_on_submit():
        data = {}
        data['name_of_part'] = form.name_of_part.data
        data['manufacturer_of_part'] = form.manufacturer_of_part.data
        # Send data from form to Database
        insert_data('orders', data)
        return redirect('/customers')
    return render_template('order.html', form=form)
