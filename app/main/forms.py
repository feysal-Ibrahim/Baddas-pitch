from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField,BooleanField,RadioField,SelectField,FileField,PasswordField,SelectField
from ..models import Pitch, Comment
from wtforms.validators import DataRequired,Required


class PitchForm(FlaskForm):
    title = StringField('Pitch Category Title', validators=[DataRequired()])
    body = TextAreaField('Enter your Pitch here', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment here', validators=[DataRequired()])
    vote = RadioField ( 'Vote ' , choices=[('upvote' , 'upvote') , ('downvote' , 'downvote')] ,
                        validators=[Required ( )] )
    submit = SubmitField('Submit')