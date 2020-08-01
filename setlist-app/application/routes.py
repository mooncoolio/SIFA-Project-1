# import render_template function from the flask module
from flask import render_template, url_for, redirect
# import the app object from the ./application/__init__.py
from application import app, db
# importing Songs and SetList Class from models.py
from application.models import Songs, SetList
# importing song form from forms.py
from application.forms import SongForm






# define routes for /,  /home, /songbank, /create, /view & /edit  this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/songbank')
def songbank():
	songData = Songs.query.all()
	return render_template('songbank.html', title='Song Bank', songs=songData)


@app.route('/addsong', methods=['GET', 'POST'])
def addsong():
	form = SongForm()
	if form.validate_on_submit():
		songData = Songs(
			song_name = form.song_name.data,
			song_album = form.song_album.data,
			song_artist = form.song_artist.data,
			song_key = form.song_key.data,
			song_bpm = form.song_bpm.data
		)
		db.session.add(songData)
		db.session.commit()
		return redirect(url_for('songbank'))
	else:
		print(form.errors)
	return render_template('addsong.html', title='Add Song', form=form)

@app.route('/create')
def create():
	return render_template('create.html', title='Create')

@app.route('/view')
def view():
	return render_template('view.html', title='View')

@app.route('/edit')
def edit():
	return render_template('edit.html', title='Edit')
