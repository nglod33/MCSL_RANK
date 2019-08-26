# Author: Nate Glod
# File: MCSL_RANK/webAPP/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField

class queryForm(FlaskForm):
    # Text Fields
    firstName = StringField('First Name')
    lastName = StringField('Last Name')
    minAge = StringField('Min Age')
    maxAge = StringField('Max Age')

    # Radio Fields
    Sex = RadioField('Sex', choices=[('Boys', 'Boys'), ('Birls', 'Girls')])
    Event = RadioField('Event', choices=[('IM', 'IM'),('Back', 'Back'), ('Breast', 'Breast'), ('Free', 'Free'), ('Fly', 'Fly')])
    Distance = RadioField('Distance', choices=[(25,'25'),(50,'50'),(100,'100')])

    # Submit button
    submit = SubmitField('Search!')
