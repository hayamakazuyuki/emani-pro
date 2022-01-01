from flask import Blueprint, request, flash, redirect, render_template, url_for
from flask_login import login_required, current_user
from sqlalchemy.sql.expression import null

from .models import Customer, Shop
from ..staff.models import Staff

from .forms import CustomerForm, ShopForm
from app import db

customer = Blueprint('customer', __name__, url_prefix='/customer')

#========== customer ==========#
@customer.route('/')
@login_required
def index():

    page = request.args.get('page', 1, type=int)
    customers = Customer.query.paginate(page=page, per_page=20)

    return render_template('customer/index.html', customers=customers, page=page)

# register contractor
@customer.route('/register', methods=['GET', 'POST'])
@login_required
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


@customer.route('/<int:id>', methods=['GET', 'POST'])
@login_required
def profile(id):

    customer = Customer.query.get_or_404(id)
    staff = Staff.query.get(customer.registered_by)
    mode = request.args.get('mode')

    page = request.args.get('page', 1, type=int)
    shops = Shop.query.filter_by(customer_id=id).paginate(page=page, per_page=20)

    if mode == 'edit':
        form = CustomerForm()

        if form.validate_on_submit():

            customer.name = request.form['name']
            customer.title = request.form.get('title')
            customer.representative = request.form['representative']
            customer.zip = request.form['zip']
            customer.prefecture = request.form['prefecture']
            customer.city = request.form['city']
            customer.town = request.form['town']
            customer.address = request.form.get('address')
            customer.bldg = request.form.get('bldg')
            customer.telephone = request.form['telephone']
            customer.registered_by = current_user.id

            is_inactive = request.form.get('is_inactive')

            if customer.is_inactive is None and is_inactive:
                customer.is_inactive = 1

            elif customer.is_inactive and is_inactive is None:
                customer.is_inactive = None

            db.session.commit()

            flash('取引先情報を更新しました。', 'success')

            return redirect(url_for('customer.profile', id=id))

        return render_template('customer/update.html', customer=customer, form=form)

    return render_template('customer/profile.html', customer=customer, staff=staff, shops=shops)


#========== shop ==========#
@customer.route('/shop/register', methods=['GET', 'POST'])
@login_required
def shop_register():

    form = ShopForm()
    customer_id = request.args.get('customer_id')

    if form.validate_on_submit():
        customer_id = request.form['customer_id']
        id = request.form['id']
        customer_shop_id = request.form.get('customer_shop_id')
        name = request.form['name']
        zip = request.form['zip']
        prefecture = request.form['prefecture']
        city = request.form['city']
        town = request.form['town']
        address = request.form['address']
        bldg = request.form.get('bldg')
        telephone = request.form['telephone']
        registered_by = current_user.id

        # check if requested shop already exists in the db
        exists = Shop.query.get((customer_id, id))

        if exists:
            return redirect(url_for('customer.shop_profile', customer_id=customer_id, id=id))

        else:
            shop = Shop(customer_id=customer_id, id=id, customer_shop_id=customer_shop_id, name=name, zip=zip,
            prefecture=prefecture, city=city, town=town, address=address, bldg=bldg, telephone=telephone, registered_by=registered_by)

            db.session.add(shop)
            db.session.commit()

            flash('事業所を登録しました。', 'success')
            return redirect(url_for('customer.profile', id=customer_id))

    return render_template('customer/shop-register.html', form=form, customer_id=customer_id)


@customer.route('/<int:customer_id>/<int:id>', methods=['GET', 'POST'])
@login_required
def shop_profile(customer_id, id):
    
    shop = Shop.query.get_or_404((customer_id, id))
    staff = Staff.query.get(shop.registered_by)

    mode = request.args.get('mode')

    if mode == 'edit':
        form = ShopForm()

        if form.validate_on_submit():

            shop.customer_id = request.form['customer_id']
            shop.id = request.form['id']
            shop.customer_shop_id = request.form.get('customer_shop_id')
            shop.name = request.form['name']
            shop.zip = request.form['zip']
            shop.prefecture = request.form['prefecture']
            shop.city = request.form['city']
            shop.town = request.form['town']
            shop.address = request.form['address']
            shop.bldg = request.form.get('bldg')
            shop.telephone = request.form['telephone']
            shop.registered_by = current_user.id

            db.session.commit()

            flash('取引先情報を更新しました。', 'success')

            return redirect(url_for('customer.shop_profile', customer_id=customer_id, id=id))

        return render_template('customer/shop-update.html', shop=shop, form=form)

    return render_template('customer/shop-profile.html', shop=shop, staff=staff)
