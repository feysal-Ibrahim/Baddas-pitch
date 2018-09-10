from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column ( db.String ( 255 ) , unique=True , index=True )
    bio = db.Column ( db.String ( 255 ) )
    profile_pic_path = db.Column ( db.String ( ) )
    pass_secure = db.Column ( db.String ( 255 ) )
    # Defining the One to many relationship between a user and a pitch
    pitch = db.relationship ( 'Pitch' , backref="user" , lazy='dynamic' )

    @property
    def password(self):
        raise AttributeError ( 'You cannot read the password attribute' )

    @password.setter
    def password(self , password):
        self.pass_secure = generate_password_hash ( password )

    def verify_password(self , password):
        return check_password_hash ( self.pass_secure , password )


    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    body = db.Column ( db.String )
    time_posted = db.Column ( db.DateTime , default=datetime.utcnow )
    # Defining the foreign key from the relationship between a user and a pitch
    user_id = db.Column ( db.Integer , db.ForeignKey ( "users.id" ) )
    # Defining the foreign key from the relationship between a pitch and a category
    category_id = db.Column ( db.Integer , db.ForeignKey ( "categories.id" ) )
    # Defining a one to many relationship between a pitch and a comment
    comments = db.relationship ( 'Comment' , backref="main_pitch" , cascade="all, delete-orphan" , lazy="dynamic" )
    def __repr__(self):
        return f'User {self.title}'

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    # Defining a one to many relationship between a category and a pitch
    pitch = db.relationship('Pitch', backref='parent_category', lazy='dynamic')

    def __repr__(self):
        return f'Category {self.name}'


class Comment(db.Model):
    __tablename__ = 'comments'

    id =  db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(255))
    comment = db.Column(db.String)
    # Defining the foreign key from the relationship between a pitch and a comment
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    # Defining the foreign key from the relationship between a user and a comment
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comment(self):
        '''
        Save the Comments/comments per pitch
        '''
        db.session.add ( self )
        db.session.commit ( )

    @classmethod
    def get_comments(self , id):
        comment = Comment.query.order_by ( Comment.time_posted.desc ( ) ).filter_by ( pitches_id=id ).all ( )
        return comment

    def __repr__(self):
        return f'Comment {self.comment}'