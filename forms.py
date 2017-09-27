# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from wtforms_components import IntegerField


class RecipeEditForm(FlaskForm):
    title = StringField(
        'Title', validators=[DataRequired]
    )

    ingridient = TextAreaField(
        'Ingridient', validators=[DataRequired]
    )

    desc = TextAreaField(
        'Desc', validators=[DataRequired]
    )