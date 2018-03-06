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
    print(form)
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        models.insert_customer((
            form.first_name.data,
            form.last_name.data,
            form.company.data,
            form.email.data,
            form.phone.data),
           (form.street_address.data,
            form.city.data,
            form.state.data,
            form.country.data,
            form.zip_code.data))

        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    print(models.retrieve_orders()[0].keys())
    print(models.retrieve_customers()[0].keys())
    return render_template('home.html',
                            customers=models.retrieve_customers(),
                            orders=models.retrieve_orders())

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    orderForm = OrderForm()
    if orderForm.validate_on_submit():
        models.insert_order(
            (orderForm.name_of_part.data,
             orderForm.manufacturer_of_part.data),
            value
        )

        return redirect('/customers')
    return render_template('order.html', form=orderForm)
