import uuid
import datetime

from app.main import db
from app.main.model.budget import Budget

# Budget fields
# id = db.Column(db.Integer, primary_key=True, autoincrement=True)
# set_on = db.Column(db.DateTime, nullable=False)
# length = db.Column(db.String, nullable=False)
# amount = db.Column(db.Float, nullable=False)
# success = db.Column(db.Boolean, nullable=False)
# user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

def save_new_budget(data):
    new_budget = Budget(
        set_on = datetime.datetime.utcnow(),
        length = data['length'],
        amount = data['amount'],
        success= data['success'],
        user_id= data['user_id']
    )
    save_changes(new_budget)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201

# TODO:
# Get budgets by day
# Get budgets by time length
# Get budgets by amount of money
# Get budgets by success

def get_all_budgets():
    return Budget.query.all()


def get_all_user_budgets(user_id):
    return Budget.query.filter_by(user_id=user_id).all()


def save_changes(data):
    db.session.add(data)
    db.session.commit()