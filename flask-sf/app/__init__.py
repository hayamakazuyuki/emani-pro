from flask import Flask

from .extentions import db, login_manager, admin

from .contractor.views import contractor
from .customer.views import customer
from .staff.views import staff
from .errors.handlers import errors


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.BaseConfig')
    

    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    login_manager.login_view = 'staff.login'
    login_manager.login_message = False


    @app.route('/')
    def index():
        return 'hi'

    app.register_blueprint(contractor)
    app.register_blueprint(customer)
    app.register_blueprint(staff)
    app.register_blueprint(errors)

    return app
