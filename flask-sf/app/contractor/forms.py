from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField
from wtforms.validators import InputRequired, NumberRange, Length, Regexp


class ContractorForm(FlaskForm):
    id = IntegerField('業者ID', validators=[InputRequired('業者IDは必須です。'),
    NumberRange(min=1, max=999999, message='範囲のIDを入力してください。')])
    name = StringField('業者名', validators=[InputRequired('業者名は必須です。')])
    title = StringField('代表者役職名')
    representative = StringField('代表者名', validators=[InputRequired('代表者名は必須です。')])
    zip = StringField('郵便番号', validators=[InputRequired('郵便番号は必須です。'),
    Length(min=7, max=7, message='郵便番号は7桁です。')])
    prefecture = StringField('都道府県', validators=[InputRequired('都道府県は必須です。')])
    city = StringField('市区町村', validators=[InputRequired('市区町村は必須です。')])
    town = StringField('町域', validators=[InputRequired('町域は必須です。')])
    address = StringField('住所', validators=[InputRequired('住所は必須です。')])
    bldg = StringField('建物名等')
    telephone = StringField('代表電話', validators=[InputRequired('電話番号は必須です。'),
    Regexp('[0-9]+-[0-9]+-[0-9+]', message='電話番号は数字-数字-数字です。')])
    is_inactive = BooleanField('休止')
    care = BooleanField('サティスケア会員')
