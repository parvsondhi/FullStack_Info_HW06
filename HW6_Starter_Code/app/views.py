from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, OrderForm
# Access the models file to use SQL functions--done
from .models import *


@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm() 
    if form.validate_on_submit():
        # Get data from the form -- done
        # Send data from form to Database -- done
        company = form.company.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone = form.phone.data
        street_address  = form.street_address.data
        city = form.city.data
        state  = form.state.data
        country  = form.country.data
        zip_code = form.zip_code.data
        insert_data(first_name, last_name, company, email, phone)
        insert_address(street_address, city, state, country, zip_code)
        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    customers =  retrieve_customers([1],[1],[1],[1],[1],)
    orders = retrieve_orders([1],[1]) 
    # Retreive data from database to display
    return render_template('home.html',
                            customers=customers, orders=orders)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    customerID = value 
    form2 = OrderForm()
    if form2.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        name_of_part = form2.name_of_part.data
        manufacturer_of_part = form2.manufacturer_of_part.data
        value = value
        insert_orders(name_of_part, manufacturer_of_part, value)
        return redirect('/customers')
    return render_template('order.html', form2=form2, value=value)
