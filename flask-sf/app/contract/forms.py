from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField
from wtforms.validators import InputRequired, NumberRange, Length, Regexp
from .models import ContractType

from wtforms_sqlalchemy.fields import QuerySelectField


def contract_type():
    return ContractType.query


class ContractRegisterForm(FlaskForm):
    opts = QuerySelectField(query_factory=contract_type, allow_blank=False)
