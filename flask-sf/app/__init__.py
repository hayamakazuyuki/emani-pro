from flask import Flask

from .extentions import db, login_manager

from .contractor.views import contractor
from .customer.views import customer


def create_app():
    app = Flask(__name__)

    db.init_app(app)
    #login_manager.init_app(app)
    # login_manager.login_view = 'staff.login'
    # login_manager.login_message = False


    @app.route('/')
    def index():
        return 'hi'

    app.register_blueprint(contractor)
    app.register_blueprint(customer)

    return app
