import uuid
import datetime

from app.main import db
from app.main.model.user import User

# import os

# # postgres_local_base = os.environ.get('DATABASE_URL')

def save_new_user(data):
    user = User.query.filter_by(username=data['username']).first()

    if not user:
      if 'email' in data:
            new_user = User(
                public_id=data['username'],
                email=data['email'],
                username=data['username'],
                password=data['password'],
                registered_on=datetime.datetime.utcnow(),
                level = 1
            )
            save_changes(new_user)
            return generate_token(new_user)
      else:
            new_user = User(
                public_id=data['username'],
                email=None,
                username=data['username'],
                password=data['password'],
                registered_on=datetime.datetime.utcnow(),
                level = 1
            )
            save_changes(new_user)
            return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401