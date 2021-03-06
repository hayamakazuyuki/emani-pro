from flask import Blueprint, render_template, request
from flask_login import login_required

from .forms import ContractRegisterForm

from ..customer.models import Customer, Shop
from ..contractor.models import Contractor

contract = Blueprint('contract', __name__, url_prefix='/contract')

#==================== contract ====================#
# contract index page
@contract.route('/')
@login_required
def index():
    return render_template('contract/index.html')


@contract.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    form = ContractRegisterForm()

    customer_id = request.args.get('customer_id')
    shop_id = request.args.get('shop_id')

    customer = Customer.query.get(customer_id)
    shop = Shop.query.get((customer_id, shop_id))

    if form.validate_on_submit():
        return request.form['opts']

    return render_template('contract/register.html', form=form, customer=customer, shop=shop)


@contract.route('/contractor_search', methods=['GET', 'POST'])
def contractor_search():

    if request.method == 'POST':
        q = request.form['q']

        value = "%{}%".format(q)
        contractors = Contractor.query.filter(Contractor.name.like(value))
        hits = contractors.count()

        if hits == 0:
            result = '別のキーワードで検索してください。'
            return render_template('contract/contractor-search.html', result=result)

        elif hits > 11:
            result = 'キーワードを絞り込んでください。'
            return render_template('contract/contractor-search.html', result=result)

        else:
            result = f'{hits}件の候補があります。'
            return render_template('contract/contractor-search.html', contractors=contractors, result=result)
        
    return render_template('contract/contractor-search.html')
