from sqlalchemy import func
from ..extentions import db, admin
# from flask_admin.contrib.sqla import ModelView


# class ContractType(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String(20), nullable=False, unique=True)


class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    shop_id = db.Column(db.Integer, nullable=False)
    contractor_id = db.Column(db.Integer, nullable=False)
    contract_type = db.Column(db.Integer, nullable=False)
    effective_date = db.Column(db.DateTime, nullable=False)
    terminate_date = db.Column(db.DateTime, nullable=True)
    auto_extension = db.Column(db.Integer, nullable=True)
    is_terminated = db.Column(db.Integer, nullable=True)
    registered_by = db.Column(db.Integer, nullable=False)
    registered_at = db.Column(db.DateTime, default=func.now())


# admin.add_view(ModelView(ContractType, db.session))
