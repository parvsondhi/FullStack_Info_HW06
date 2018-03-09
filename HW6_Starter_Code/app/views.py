from flask import render_template, redirect, request, abort, session
from app import app, models, db
from .forms import CustomerForm, OrderForm, AddressForm
from .utils import dict_to_obj, flash_message


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
    return render_template('home.html', customers=customers, orders=orders, flash_message=flash_message(session))

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    ''' Create a new customer '''
    form = CustomerForm()
    if form.validate_on_submit():
        customer_id = models.insert_customer(form)
        if customer_id:
            flash_message(session, text='<strong>Success!</strong> Customer was created.')
            return redirect('/customers/'+str(customer_id))
        else: 
            return redirect('/customers')
    return render_template('customer.html', form=form, flash_message=flash_message(session))

@app.route('/customers/<id>', methods=['GET', 'POST'])
def edit_customer(id):
    ''' Edit and update an existing customer '''
    customer = models.retrieve_one_customer_by_id(id)
    if (customer is None):
        abort(404)

    form = CustomerForm(obj=dict_to_obj(customer))
    addressForm = AddressForm()
    if len(customer['addresses']):
        addressForm = AddressForm(obj=dict_to_obj(customer['addresses'][0]))

    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        models.update_customer(id, form)
        flash_message(session, text='<strong>Success!</strong> Customer was updated.')
        return redirect('/customers/' + str(id))

    return render_template('customer-detail.html', form=form, customer=customer, addressForm=addressForm, flash_message=flash_message(session))

# ================
# ORDERS
# ================
@app.route('/customers/<customer_id>/create_order', methods=['GET', 'POST'])
def create_order(customer_id):
    ''' Create a new order '''
    form = OrderForm()
    customer = models.retrieve_one_customer_by_id(customer_id)
    if (customer is None):
        abort(404)
    if form.validate_on_submit():
        
        order_id = models.insert_order(customer['customer_id'], form)
        if order_id:
            flash_message(session, text='<strong>Success!</strong> Order was created.')
            return redirect('/orders/' + str(order_id))
        else: 
            return redirect('/customers')

    return render_template('order.html', form=form, customer=customer, flash_message=flash_message(session))


@app.route('/orders/<id>/', methods=['GET', 'POST'])
def edit_order(id):
    customers = models.retrieve_customers()
    order = models.retrieve_one_order_by_id(id)
    if (order is None):
        abort(404)

    associated_customers_with_order_ids = [c['customer_id'] for c in order['customers']]
    customers = [c for c in customers if c['customer_id'] not in associated_customers_with_order_ids]

    form = OrderForm(obj=dict_to_obj(order))

    if form.validate_on_submit():
        models.update_order(id, form)
        flash_message(session, text='<strong>Success!</strong> Order was updated.')
        return redirect('/orders/' + str(id))

    return render_template('order-detail.html',  form=form, order=order, customers=customers, flash_message=flash_message(session))


# ================
# Addresses
# ================

@app.route('/customers/<customer_id>/address', methods=['GET', 'POST'])
def create_address_for_customer(customer_id):
    customer = models.retrieve_one_customer_by_id(customer_id)
    if (customer is None):
        abort(404)

    form = AddressForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        models.insert_address_for_customer(customer['customer_id'], form)
        flash_message(session, text='<strong>Success!</strong> Address was created.')
        return redirect('/customers/' + str(customer_id))

    return redirect('/customers/' + str(customer_id))
    

@app.route('/customers/<customer_id>/address/<address_id>', methods=['GET', 'POST'])
def update_address_for_customer(customer_id, address_id):
    customer = models.retrieve_one_customer_by_id(customer_id)
    if (customer is None):
        abort(404)

    address = models.retrieve_one_addresss_by_id(address_id)
    if (address is None):
        abort(404)

    form = AddressForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        models.update_address(address['id'], form)
        flash_message(session, text='<strong>Success!</strong> Address was updated.')
        return redirect('/customers/' + str(customer_id))

    return redirect('/customers/' + str(customer_id))
    
