from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique = True,index=True)
    comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'))
   # bio = db.Column(db.String(255))
    #profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))

    @property
    def password(self):
         raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)     

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    def __repr__(self):
        return f'User {self.username}'

class Comment(db.Model):
        __tablename__= 'comments'
        id = db.Column(db.Integer,primary_key = True)
        comment =   db.Column(db.String(255)) 
        users = db.relationship('User',backref ='comment',lazy="dynamic")

        def __repr__(Self):
            return f'User{self.comment}'

class Writer(db.Model):
    __tablename__ = 'writers'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True)
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    
    def __repr__(self):
        return f'Writer {self.username}'

class Blog(db.Model):
        __tablename__= 'blogs'
        id = db.Column(db.Integer,primary_key = True)
        blog =   db.Column(db.String(255)) 
        writers = db.relationship('Writer',backref ='blog',lazy="dynamic")

        def __repr__(Self):
            return f'Writer{self.blog}'

