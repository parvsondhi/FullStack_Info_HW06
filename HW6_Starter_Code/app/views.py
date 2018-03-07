from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm
# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/customers')

@app.route('/customers')
def index_customers():
    ''' Return a list of all customers '''
    # Retreive data from database to display
    customers = models.retrieve_customers()
    orders = models.retrieve_orders()
    return render_template('home.html', customers=customers, orders=orders)

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    ''' Create a new customer '''
    form = CustomerForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        models.insert_customer(form)
        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers/<id>', methods=['GET', 'POST'])
def edit_customer(id):
    ''' Edit and update an existing customer '''
    return 'TODO: Display One Customer'

@app.route('/customers/<id>', methods=['DELETE'])
def delete_customer(id):
    return 'TODO: Delete customer'

@app.route('/customer/<customer_id>/create_order', methods=['GET', 'POST'])
def create_order(customer_id):
    return 'TODO: Create Order For Customer ' + customer_id
        # Get data from the form
        # Send data from form to Database
        # return redirect('/customers')
    return render_template('order.html', form=orderForm)
