from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    messages = db.relationship('Message', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.email


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # time_sent = db.Column(db.DateTime(timezone=True), onupdate=func.now())


class Counters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.Integer)
    sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
