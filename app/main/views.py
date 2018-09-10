from flask import render_template, url_for, flash, redirect, request, abort
from . import main
from flask_login import login_required, current_user
from app.models import User, Category, Pitch, Comment
from .forms import PitchForm,CommentForm,UpdateProfile
from .. import db


@main.route('/')
def index():
    '''
   view function that defines the routes decorater for the index
    '''


    title = 'Home - Welcome to The best Movie Review Website Online'

    return render_template ( 'index.html' , title=title)

@main.route('/pitch//new', methods = ['GET','POST'])
@login_required
def new_pitch():
    '''
       view function that defines the routes decorater for the pitch
        '''

    form = PitchForm ()
    if form.validate_on_submit():
        pitches = Pitch ( title=form.title.data , body=form.body.data )
        db.session.add (pitches)
        db.session.commit ()
        flash ( 'Your pitch has been created succesfully' )
        return redirect ( url_for ( 'main.new_pitch' ) )
    title = "Create a Pitch"
    pitches = Pitch.query.all ()

    return render_template ('pitch.html' , title=title , form=form , pitch_list=pitches )

@main.route('/comment/new', methods = ["GET", "POST"])
@login_required
def new_comment():
    '''
      view  function that defines the routes decorater for the comments
        '''

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = Comment(comment=comment_form.comment.data)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been posted succesfully')
        return redirect(url_for('main.new_comment'))
    comments = Comment.query.all()
    return render_template('comment.html', comment_form=comment_form, comment_list=comments)


@main.route('/user/<uname>')
def profile(uname):
    '''
          view  function that defines the routes decorater for the profile
            '''

    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):

    '''
          view  function for update profile
            '''


    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)





