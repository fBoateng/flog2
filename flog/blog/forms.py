from flask_wtf import FlaskForm
from wtforms import validators, StringField, TextAreaField, FileField
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_wtf.file import FileAllowed

from blog.models import Category


class PostForm(FlaskForm):
    image = FileField('Image',
                      validators=[FileAllowed(['jpg', 'png'], 'We only accept JPG or PNG images')])
    title = StringField('Title', [
        validators.InputRequired(),
        validators.Length(max=80)
    ])
    body = TextAreaField('Content', validators=[validators.InputRequired()])
    category = QuerySelectField('Category', query_factory=lambda: Category.query, allow_blank=True)
    new_category = StringField('New Category')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)


def validate(self, extra_validators=None):
    if not self.category.data and not self.new_category.data:
        self.category.errors.append('You must select or create a category')
        return False
    return True
