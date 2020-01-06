from flask_restplus import Namespace, fields

class AuthDto:
    api = Namespace('auth', description='authentication operations')
    user_auth = api.model('auth', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
    
class UserDto:
    api = Namespace('user', description='user operations')
    user = api.model('user', {
        'fname': fields.String(required=True, description='user first name'),
        'lname': fields.String(required=True, description='user last name'),
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password')
        # TODO: plaid token
        # TODO: phone numbers for texting updates
    })
