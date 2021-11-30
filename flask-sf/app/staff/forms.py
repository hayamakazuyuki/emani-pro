from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    email = StringField('メールアドレス', validators=[InputRequired('メールアドレスは必須です。')])
    password = PasswordField('パスワード', validators=[InputRequired('パスワードを入力してください。')])


