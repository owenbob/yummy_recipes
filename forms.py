# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


"""
 class form that defines what the form is made of
 particularly
"""
class RecipeEditForm(FlaskForm):
    title = StringField(
        'Title', validators=[DataRequired()]
    )

    ingridient = TextAreaField(
        'Ingridient', validators=[DataRequired()]
    )

    desc = TextAreaField(
        'Desc', validators=[DataRequired()]
    )