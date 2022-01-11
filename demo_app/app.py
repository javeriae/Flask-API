import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()


def get_database_url():
    db_name = os.environ.get('DB_NAME')
    db_host = os.environ.get('DB_HOST')
    db_password = os.environ.get('DB_PASSWORD')
    db_user = os.environ.get('DB_USER')
    return f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"


def init_app():
    """Initialize the core application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = get_database_url()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import models, routes

        # Register Blueprints
        app.register_blueprint(routes.home_bp)

        return app
