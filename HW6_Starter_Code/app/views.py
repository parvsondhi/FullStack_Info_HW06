from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, OrderForm
# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        # Get data from the form
        company = form.company.data
        email = form.email.data
        first = form.first_name.data
        last = form.last_name.data
        phone = form.phone.data


        street_address = form.street_address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zip_code = form.zip_code.data
        



        models.insert_customer_data(company,email, first, last, phone, street_address, city, state, country, zip_code)
        # Send data from form to Database
        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = models.retrieve_customers()
    orders = models.retrieve_orders()
    return render_template('home.html',
                            customers=customers, orders=orders)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):

    orderform = OrderForm()
    if orderform.validate_on_submit():
        part_name  = orderform.part_name.data
        manufacturer  = orderform.manufacturer.data
        # Get data from the form
        # Send data from form to Database
        models.insert_order_data(value, part_name, manufacturer)
        return redirect('/customers')
    return render_template('order.html', form=orderform)
