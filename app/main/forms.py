from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField,BooleanField,RadioField,SelectField,FileField,PasswordField,SelectField
from ..models import Pitch, Comment
from wtforms .validators import DataRequired,Required

'''
1.form flask_wtforms impot flaskform,StringField, TextAreaField,SubmitField,BooleanField,RadioField,SelectField,FileField,PasswordField,SelectField,.validators import DataRequired,Required
2.from models import pitch class and comment 
'''


class PitchForm(FlaskForm):
    title = StringField('Pitch Category Title', validators=[DataRequired()])
    body = TextAreaField('Enter your Pitch here', validators=[DataRequired()])
    submit = SubmitField('Submit')

    '''
    crate the inputs for comments form with vite options
    '''

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment here', validators=[DataRequired()])
    vote = RadioField ( 'Vote ' , choices=[('upvote' , 'upvote') , ('downvote' , 'downvote')] ,
                        validators=[Required ( )] )
    submit = SubmitField('Submit')

    '''
    crate the inputs for comments form with vite options
    '''

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

    '''
     create a new form class UpdateProfile that has only the bio Textarea form field.
    '''