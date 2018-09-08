from flask import Blueprint
main=Blueprint('main',__name__)
'''
create an instance of the main and set it as blueprint
'''
from . import views,error,forms
'''
import views.py,errors.py and form.py from main folder in the app folder
'''