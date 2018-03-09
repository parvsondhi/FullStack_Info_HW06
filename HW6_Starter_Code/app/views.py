from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, OrderForm
from .models import *
# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    # customerForm = CustomerForm()
    # addressForm = AddressForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        first_name = form.first_name.data # getting data from html 
        last_name = form.last_name.data
        company = form.company.data
        email = form.email.data
        phone_number = form.phone_number.data
        # insert into models.py
        customer_id = insert_customer(first_name,last_name,company,email,phone_number)
        
        
        street_address = form.street_address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zip_code = form.zip_code.data
        insert_address(street_address,city,state,country,zip_code, customer_id)
        
        return redirect('/customers')
    return render_template('customers.html', form=form)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customer = retrieve_customers()
    order = retrieve_orders()
    return render_template('home.html',
                            customer=customer, orders=order)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    # Get data from the form
    # Send data from form to Database
    orderForm = OrderForm()
    if orderForm.validate_on_submit():
        customer_id = value
        name_of_part = orderForm.name_of_part.data
        manufacturer_of_part = orderForm.manufacturer_of_part.data
        order_id = insert_order(name_of_part, manufacturer_of_part)
        insert_customer_orders(customer_id, order_id)
        return redirect('/customers')
    return render_template('order.html', form=orderForm)