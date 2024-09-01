from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
db =SQLAlchemy()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    workouts= db.relationship('Workout', backref='author', lazy=True)


class Workout(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    sets =db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    workout_name =db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)