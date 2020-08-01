from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

#creating a back end form to allow for song details to be input
class SongForm(FlaskForm):
	song_name = StringField('Song Name',
                validators = [
                        DataRequired(),
                        Length(min=2, max=100)
                ]
        )
	song_album = StringField('Album',
                validators = [
                        DataRequired(),
                        Length(min=2, max=100)
                ]
        )
	song_artist = StringField('Artist',
                validators = [
                        DataRequired(),
                        Length(min=2, max=100)
                ]
        )
	song_key = StringField('Key',
                validators = [
                        DataRequired(),
                        Length(min=2, max=10)
                ]
        )
	song_bpm = IntegerField('BPM',
                validators = [
                        DataRequired(),
                ]
        )
	
	submit = SubmitField('Add Song')
