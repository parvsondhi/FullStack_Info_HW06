from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, orderForm
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
        telephone = form.telephone.data
        # Modded this
        customerID = insert_customer(firstName, lastName, company, email, telephone)
        # Added this
        addressID = customerID[0]

        # Get ID of current customer being created and insert address data to the db
        # Commented this out
        # addressID = retrieve_customer_id(firstName, lastName)['customer_id']
        streetAddress = form.streetAddress.data
        state = form.state.data
        country = form.country.data
        zipCode = form.zipCode.data
        insert_address(addressID, streetAddress, state, country, zipCode)

        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()

    orders = retrieve_orders()

    

    stuff = []

    i=0
    for order in orders:
        oID = order['order_id']
        customerID = retrieve_order_match(oID)

        bob = {}
        bob['name_of_part'] = order['name_of_part']
        bob['manufacturer_of_part'] = order['manufacturer_of_part']
        bob['customer_id'] = customerID[0]
        
        stuff.append(bob)    

    return render_template('home.html', customers=customers, orders=stuff)


# THIS WAS HERE BUT COMMENTED OUT MOMNTARILLY

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    form = orderForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        nameOfPart = form.nameOfPart.data
        manufacturerOfPart = form.manufacturerOfPart.data
        
        orderID = insert_order(nameOfPart, manufacturerOfPart)
        orderID = orderID[0]
        
        customerID = retrieve_customer_id_byemail(value)
        customerID = customerID['customer_id']
        
        insert_order_match(orderID, customerID)

        return redirect('/customers')
    return render_template('order.html', form=form)
