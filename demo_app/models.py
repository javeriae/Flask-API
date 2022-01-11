from datetime import datetime

from .app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    country = db.Column(db.String(20), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
