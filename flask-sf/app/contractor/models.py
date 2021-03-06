from sqlalchemy import func
from ..extentions import db, admin
from flask_admin.contrib.sqla import ModelView


class Contractor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(50), nullable=True)
    representative = db.Column(db.String(50), nullable=False)
    zip = db.Column(db.String(7), nullable=False)
    prefecture = db.Column(db.String(4), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100))
    bldg = db.Column(db.String(50))
    telephone = db.Column(db.String(15), nullable=False)
    is_inactive = db.Column(db.Integer, nullable=True)
    registered_by = db.Column(db.Integer, nullable=False)
    registered_at = db.Column(db.DateTime, default=func.now())
    satiscare = db.relationship('Satiscare', backref='contractor', uselist=False)

class Satiscare(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contractor_id = db.Column(db.Integer, db.ForeignKey('contractor.id'), unique=True, nullable=False)
    membership = db.Column(db.Integer, nullable=True)

admin.add_view(ModelView(Contractor, db.session, endpoint="contractorview"))
admin.add_view(ModelView(Satiscare, db.session, endpoint="satiscare"))
