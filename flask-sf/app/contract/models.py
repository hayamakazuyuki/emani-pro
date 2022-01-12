from ..extentions import db, admin
from flask_admin.contrib.sqla import ModelView

class ContractType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False, unique=True)

admin.add_view(ModelView(ContractType, db.session))
