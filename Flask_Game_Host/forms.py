from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, validators, ValidationError

class GameForm(FlaskForm):

    name = StringField('Name', validators=[validators.InputRequired()])
    display_name = StringField('Display Name', validators=[validators.InputRequired()])
    open_source = BooleanField('Open Source')
    img_name = StringField('Name of Image File', validators=[validators.InputRequired()])
    url = StringField('URL', validators=[validators.InputRequired()])
    embed_link = StringField('Embed Link', validators=[validators.InputRequired()])
    submit = SubmitField('Add Game')