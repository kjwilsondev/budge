from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..util.dto import BudgetDto
from ..service.user_service import save_new_user, get_all_users, get_a_user
from ..service.budget_service import save_new_budget, get_all_budgets, get_all_user_budgets

api = BudgetDto.api
_user = UserDto.user
_budget = BudgetDto.budget