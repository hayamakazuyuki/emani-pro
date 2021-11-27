from flask import Flask

from .contractor.views import contractor


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'hi'

    app.register_blueprint(contractor)
    
    return app
