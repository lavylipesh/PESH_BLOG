from  flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import Required
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
  title = StringField('Title',validators=[Required()])
  pitch = TextAreaField('Write a blog',validators=[Required()])
  submit = SubmitField('submit')

class CommentForm(FlaskForm):
  comments = TextAreaField('Your comment here',validators=[Required()])
  author = StringField('Author',validators=[Required()])
  submit = SubmitField('submit')