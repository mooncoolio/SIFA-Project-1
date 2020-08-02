# import render_template function from the flask module
from flask import render_template, url_for, redirect, request
# import the app object from the ./application/__init__.py
from application import app, db
# importing Songs and SetList Class from models.py
from application.models import Songs, SetList, setlink
# importing song form from forms.py
from application.forms import SongForm, SetForm, UpdateSongForm






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

@app.route('/songbank/delete/<id>', methods=['GET', 'POST'])
def song_delete(id):
	song = Songs.query.filter_by(id=id).first()
	db.session.delete(song)
	db.session.commit()
	return redirect(url_for('songbank'))

@app.route('/songbank/edit/<id>', methods=['GET', 'POST'])
def song_edit(id):
	song = Songs.query.filter_by(id=id).first()
	form = UpdateSongForm()
	if form.validate_on_submit():
		song.song_name = form.song_name.data
		song.song_album = form.song_album.data
		song.song_artist = form.song_artist.data
		song.song_key = form.song_key.data
		song.song_bpm = form.song_bpm.data
		song.song_bpm = form.song_bpm.data
		db.session.commit()
		return redirect(url_for('songbank'))
	elif request.method == 'GET':
		form.song_name.data = song.song_name
		form.song_album.data = song.song_album
		form.song_artist.data =	song.song_artist
		form.song_key.data = song.song_key
		form.song_bpm.data = song.song_bpm
	return render_template('editsong.html', title ='Edit Song', form=form)
	
		

@app.route('/create', methods=['GET', 'POST'])
def create():
	form = SetForm()
	if form.validate_on_submit():
		setData = SetList(
			set_name = form.set_name.data
		)
		db.session.add(setData)
		db.session.commit()
		return redirect(url_for('create'))
	else:
		print(form.errors)
	return render_template('create.html', title='Create', form=form)



@app.route('/view')
def view():
        setData = SetList.query.all()
        return render_template('view.html', title='View', set_list=setData)

@app.route('/view/addsetsong')
def addsetsong():
	songData = Songs.query.all()
	return render_template("addsongbank.html", title="addsetsong", song=songData)


@app.route('/edit')
def edit():
	return render_template('edit.html', title='Edit')
