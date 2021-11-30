from werkzeug.security import generate_password_hash, check_password_hash
from ..extentions import db, login_manager, admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import event


from flask_login import UserMixin


class Staff(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    inactive = db.Column(db.Boolean, nullable=True)

    def check_password(self, password):
        return check_password_hash(self.password, password)

@event.listens_for(Staff.password, 'set', retval=True)
def hash_staff_password(target, value, oldvalue, initiator):
    if value != oldvalue:
        return generate_password_hash(value)
    return value


@login_manager.user_loader
def load_user(user_id):
    return Staff.query.get(user_id)


admin.add_view(ModelView(Staff, db.session, endpoint="staffview"))
