from flask import Blueprint, render_template, request
from flask_login import login_required

from .forms import ContractRegisterForm

from ..customer.models import Customer, Shop

contract = Blueprint('contract', __name__, url_prefix='/contract')

#==================== contract ====================#
# contract index page
@contract.route('/')
@login_required
def index():
    return render_template('contract/index.html')



@contract.route('/register')
@login_required
def register():
    form = ContractRegisterForm()

    customer_id = request.args.get('customer_id')
    shop_id = request.args.get('shop_id')

    customer = Customer.query.get(customer_id)
    shop = Shop.query.get((customer_id, shop_id))

    return render_template('contract/register.html', form=form, customer=customer, shop=shop)
