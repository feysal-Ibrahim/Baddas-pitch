from flask import Blueprint
main=Blueprint('main',__name__)
'''
like the auth folder create an instance of the main folder and set it as blueprint
'''
from . import views,error,forms
'''
from main,import views.errors and form.py
'''