from flask import Blueprint, request, flash, redirect, render_template, url_for
from .forms import CustomerForm


customer = Blueprint('customer', __name__, url_prefix='/customer')


# customer index route
@customer.route('/')
def index():
    return render_template('customer/index.html')


#    form = CustomerForm()

#    return render_template('customer/register.html', form=form)

    """
    page = request.args.get('page', 1, type=int)
    customers = Customer.query.paginate(page=page, per_page=20)

    return render_template('customer/index.html', customers=customers)
"""

@customer.route('/shop')
def shop():
    return 'ショップ'
