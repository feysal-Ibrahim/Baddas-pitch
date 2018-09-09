from flask import Blueprint

auth = Blueprint('auth',__name__)

'''
like in the main folder create an instance of the auth folder and set it as blueprint
'''

from . import views,forms

'''
from auth,import views.errors and form.py
'''