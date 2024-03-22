from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL,NumberRange,Length

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])

    species = SelectField("Species", choices=[('cat','Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0,max=30)])

    notes = StringField("Notes", validators=[Optional(), Length(min=10)])


class EditPetForm(FlaskForm):
    photo_url = StringField("Photo_url", validators=[Optional(), URL()])

    notes = StringField("notes", validators=[Optional(), Length(min=10)])

    available = BooleanField("Available?")

