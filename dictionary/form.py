from flask_wtf import FlaskForm
from wtforms import StringField, validators


class DictionaryForm(FlaskForm):

    word = StringField("Word", validators=[validators.DataRequired()])