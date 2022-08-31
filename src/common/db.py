from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, upgrade, downgrade


db: SQLAlchemy = SQLAlchemy()
ma: Marshmallow = Marshmallow()
migrate: Migrate = Migrate()


def alembic_upgrade(app: Flask):
    """Upgrades the database to the latest revision"""
    with app.app_context():
        upgrade()


def alembic_downgrade(app: Flask):
    """Downgrades the database to the previous revision"""
    with app.app_context():
        downgrade()
