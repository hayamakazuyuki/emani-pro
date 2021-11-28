from flask import Blueprint, request, flash, redirect, render_template, url_for
from .models import Customer
from .forms import CustomerForm
from app import db


customer = Blueprint('customer', __name__, url_prefix='/customer')


# customer index route
@customer.route('/')
def index():
    return render_template('customer/index.html')




    """
    page = request.args.get('page', 1, type=int)
    customers = Customer.query.paginate(page=page, per_page=20)

    return render_template('customer/index.html', customers=customers)
"""

# register contractor
@customer.route('/register', methods=['GET', 'POST'])
def register():
    form = CustomerForm()

    if form.validate_on_submit():
        id = request.form['id']

        # check if id already exists in the db
        exists = Customer.query.get(id)

        if exists:
            return '登録済みです'

        else:
            name = request.form['name']
            title = request.form.get('title')
            representative = request.form['representative']
            zip = request.form['zip']
            prefecture = request.form['prefecture']
            city = request.form['city']
            town = request.form['town']
            address = request.form.get('address')
            bldg = request.form.get('bldg')
            telephone = request.form['telephone']
            registered_by = current_user.id

            customer = Customer(id=id, name=name, title=title, representative=representative, zip=zip,
             prefecture=prefecture, city=city, town=town, address=address, bldg=bldg, telephone=telephone, registered_by=registered_by)

            db.session.add(customer)
            
            db.session.commit()

            flash('取引先を登録しました。', 'success')

            return redirect(url_for('customer.index'))

    return render_template('customer/register.html', form=form)



@customer.route('/customer/<int:id>')
def customer_profile(id):
    customer = Customer.query.get_or_404(id)
    
    return render_template('customer/profile.html', customer=customer)


@customer.route('/shop')
def shop():
    return 'ショップ'
