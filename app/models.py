from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique = True,index=True)
    comment= db.relationship('Comment',backref='user',lazy = "dynamic")
    blog= db.relationship('Blog',backref='user',lazy = "dynamic")
    pass_secure = db.Column(db.String(255))

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



class Blog(db.Model):
        __tablename__= 'blogs'
        id = db.Column(db.Integer,primary_key = True)
        author = db.Column(db.String(255))
        blog =   db.Column(db.String(255))
        user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
        comment = db.relationship('Comment',backref ='blog',lazy="dynamic")
        def save_blog(self):
            db.session.add(self)
            db.session.commit()
        @classmethod
        def get_blog(id):
            blog = Blog.query.order_by(blog_id = id).desc().all()
            return blogs

        def __repr__(self):
            return f'Writer{self.blog}'

class Comment(db.Model):
        __tablename__= 'comments'
        id = db.Column(db.Integer,primary_key = True)
        comment =   db.Column(db.String(255))
        user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
        blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
        
        def save_comment(self):
            db.session.add(self)
            db.session.commit()
        
        def __repr__(Self):
            return f'Comment{self.comment}'
