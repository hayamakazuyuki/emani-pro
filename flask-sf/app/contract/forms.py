from random import choices
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField, DateField, RadioField
from wtforms.validators import InputRequired, NumberRange, Length, Regexp
# from .models import ContractType

# from wtforms_sqlalchemy.fields import QuerySelectField


# def contract_type():
#     return ContractType.query


# class ContractRegisterForm(FlaskForm):
#     contractor_id = IntegerField('パートナーID')
#     type = QuerySelectField('契約種別', query_factory=contract_type, allow_blank=False, get_label='type')


class ContractRegisterForm(FlaskForm):
    contractor_id = IntegerField('パートナーID',[InputRequired()])
    contract_type = RadioField('契約種別', choices=[('1', '処分'),('2', '収集運搬')])
    effective_date = DateField('契約開始日', [InputRequired()])
    terminate_date = DateField('契約終了日', [InputRequired()])
    auto_extension = BooleanField('契約自動更新')
    is_terminated = BooleanField('契約終了')
