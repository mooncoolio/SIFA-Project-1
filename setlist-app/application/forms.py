from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

#creating a back end form to allow for song details to be input
class SongForm(FlaskForm):
	song_keys = [('C', 'C'),
			('G','G'),
			('D','D'),
			('A','A'),
			('E','E'),
			('B/Cb','B/Cb'),
                        ('Gb/F#','Gb F#'),
                        ('Db/C#','Db/C#'),
			('Ab','Ab'),
                        ('Eb','Eb'),
			('F','F'),
                        ('Am','Am'),
                        ('Em','Em'),
			('Bm','Bm'),
                        ('F#m','F#m'),
                        ('C#m','C#m'),
                        ('G#m','G#m'),
			('Ebm','Ebm'),
                        ('Bbm','Bbm'),
			('Fm','Fm'),
                        ('Cm','Cm'),
			('Gm','Gm'),
                        ('Dm','Dm')
                        ]
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
	song_key = SelectField('Key',
		choices=song_keys,
                validators = [
                        DataRequired(),
                ]
        )
	song_bpm = IntegerField('BPM',
                validators = [
                        DataRequired(),
                ]
        )
	
	submit = SubmitField('Add Song')

class SetForm(FlaskForm):
	set_name = StringField('Set Name',
		validators = [
			DataRequired(),
			Length(min=2, max=100)

		]
	)

	submit = SubmitField('Create Setlist')

class UpdateSongForm(FlaskForm):
	song_keys = [('C', 'C'),
			('G','G'),
			('D','D'),
			('A','A'),
			('E','E'),
			('B/Cb','B/Cb'),
                        ('Gb/F#','Gb F#'),
                        ('Db/C#','Db/C#'),
			('Ab','Ab'),
                        ('Eb','Eb'),
			('F','F'),
                        ('Am','Am'),
                        ('Em','Em'),
			('Bm','Bm'),
                        ('F#m','F#m'),
                        ('C#m','C#m'),
                        ('G#m','G#m'),
			('Ebm','Ebm'),
                        ('Bbm','Bbm'),
			('Fm','Fm'),
                        ('Cm','Cm'),
			('Gm','Gm'),
                        ('Dm','Dm')
                        ]
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
	song_key = SelectField('Key',
		choices=song_keys,
                validators = [
                        DataRequired(),
                ]
        )
	song_bpm = IntegerField('BPM',
                validators = [
                        DataRequired(),
                ]
        )
	
	submit = SubmitField('Update Song')

class UpdateSetNameForm(FlaskForm):
        set_name = StringField('Set Name',
                validators = [
                        DataRequired(),
                        Length(min=2, max=100)

                ]
        )

        submit = SubmitField('Update Setlist Name')

class SongSetForm(FlaskForm):
	linksong  = IntegerField('Song ID',
                validators = [
                        DataRequired(),
                ]
        )
	linkset = IntegerField('Set ID',
                validators = [
                        DataRequired(),
                ]
        )
	submit = SubmitField('Add Song To Set')


