from flask import render_template, redirect, request, abort
from app import app, models, db
from .forms import CustomerForm, OrderForm
# Access the models file to use SQL functions

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

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
    ''' Create a new order '''
    form = OrderForm()
    customer = models.retrieve_customer(customer_id)
    if (customer is None):
        abort(404)
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        models.insert_order(customer['customer_id'], form)
        return redirect('/customers')
    return render_template('order.html', form=form, customer=customer)
