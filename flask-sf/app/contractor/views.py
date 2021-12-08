from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from app import db

from .forms import ContractorForm
from .models import Contractor, Satiscare
from ..staff.models import Staff


contractor = Blueprint('contractor', __name__, url_prefix='/contractor')


#==================== contractor ====================#
# contractor index page
@contractor.route('/')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    contractors = Contractor.query.paginate(page=page, per_page=20)

    return render_template('contractor/index.html', contractors=contractors)


# register contractor
@contractor.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    form = ContractorForm()

    if form.validate_on_submit():
        id = request.form['id']
        
        # check if id already exists in the db
        exists = Contractor.query.get(id)

        if exists:
            return 'あります'
        
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
            care = request.form.get('care')

            contractor = Contractor(id=id, name=name, title=title, representative=representative, zip=zip,
             prefecture=prefecture, city=city, town=town, address=address, bldg=bldg, telephone=telephone, registered_by=registered_by)

            db.session.add(contractor)
            
            if care:
                care = Satiscare(contractor_id=id, membership=care)
                db.session.add(care)

            db.session.commit()

            flash('パートナーを登録しました。', 'success')

            return redirect(url_for('contractor.index'))

    return render_template('contractor/register.html', form=form)


# show and update contractor's profile
@contractor.route('/<int:id>', methods=['GET', 'POST'])
@login_required
def profile(id):

    contractor = Contractor.query.get_or_404(id)
    staff = Staff.query.get(contractor.registered_by)
    mode = request.args.get('mode')

    if mode == 'edit':
        form = ContractorForm()

        if form.validate_on_submit():

            contractor.name = request.form['name']
            contractor.title = request.form.get('title')
            contractor.representative = request.form['representative']
            contractor.zip = request.form['zip']
            contractor.prefecture = request.form['prefecture']
            contractor.city = request.form['city']
            contractor.town = request.form['town']
            contractor.address = request.form.get('address')
            contractor.bldg = request.form.get('bldg')
            contractor.telephone = request.form['telephone']
            contractor.registered_by = current_user.id
            
            # if care checkbox is checked
            care = request.form.get('care')

            # if already a satiscare member 
            is_member = Satiscare.query.filter_by(contractor_id=id).first()

            if is_member and not care:
                member = Satiscare.query.filter_by(contractor_id=id).first()
                db.session.delete(member)

            elif not is_member and care:
                care = Satiscare(contractor_id=id, membership=care)
                db.session.add(care)

            else:
                pass

            db.session.commit()

            return redirect(url_for('contractor.profile', id=id))

        return render_template('contractor/update.html', form=form, contractor=contractor)

    return render_template('contractor/profile.html', contractor=contractor, staff=staff)

#==================== contractor ====================#

