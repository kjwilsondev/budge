from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..util.dto import BudgetDto
from ..service.user_service import save_new_user, get_all_users, get_a_user
from ..service.budget_service import save_new_budget, get_all_budgets, get_all_user_budgets

api = UserDto.api
_user = UserDto.user
_budget = BudgetDto.budget


@api.route('/')
class UserList(Resource):
    @api.doc('list of registered users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)

@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user

# @api.route('/<public_id>/budgets')
# @api.param('public_id', 'The User identifier')
# @api.response(404, 'User not found.')
# class User(Resource):
#     @api.doc('get a users list of budgets')
#     @api.marshal_with(_budget)
#     def get(self, public_id):
#         """get a users budgets given their identifier"""
#         user = get_a_user(public_id)
#         if not user:
#             api.abort(404)
#         else:
#             budgets = get_all_user_budgets(public_id)
#             return budgets

#     @api.response(201, 'Budget successfully created.')
#     @api.doc('create a new budget')
#     @api.expect(_budget, validate=True)
#     def post(self):
#         """Creates a new Budget """
#         data = request.json
#         return save_new_budget(data=data)