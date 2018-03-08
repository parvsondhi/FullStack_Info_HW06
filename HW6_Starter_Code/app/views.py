from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, OrderForm
# Access the models file to use SQL functions
from models import insert_customer_data, insert_order_data, retrieve_customers, retrieve_orders

@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database

        customer_data = (
            form.first_name.data,
            form.last_name.data,
            form.company.data,
            form.email.data,
            form.phone.data,

            form.street.data,
            form.city.data,
            form.state.data,
            form.country.data,
            form.zipcode.data,
        )
        insert_customer_data(customer_data)
        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()
    customer_dicts = []
    for customer in customers:
        customer_dict = {
            'customer_id': customer[0],
            'first_name': customer[1],
            'last_name': customer[2],
            'company': customer[3],
            'email': customer[4],
            'phone': customer[5]
        }
        customer_dicts.append(customer_dict)

    orders = retrieve_orders()
    order_dicts = []
    for order in orders:
        order_dict = {
            'part_name': order[0],
            'manufacturer': order[1],
            'customer_id': order[2]
        }
        order_dicts.append(order_dict)

    return render_template('home.html', customers=customer_dicts, orders=order_dicts)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    form = OrderForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        order_data = (
            form.part_name.data,
            form.manufacturer.data,
            value
        )
        insert_order_data(order_data)
        return redirect('/customers')
    return render_template('order.html', form=form)
