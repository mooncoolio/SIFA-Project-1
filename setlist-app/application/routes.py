# import render_template function from the flask module
from flask import render_template, url_for, redirect, request
# import the app object from the ./application/__init__.py
from application import app, db
# importing Songs and SetList Class from models.py
from application.models import Songs, SetList, SetLink
# importing song form from forms.py
from application.forms import SongForm, SetForm, UpdateSongForm, UpdateSetNameForm, SongSetForm






# define routes for homepage to be displayed
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

#define route to display song bank and display all data from songbank
@app.route('/songbank')
def songbank():
	songData = Songs.query.all()
	return render_template('songbank.html', title='Song Bank', songs=songData)

#define route to display form which will allow users to add songs to song bank
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

#define route which will allow user to delete song and any instances of the song in the link table
@app.route('/songbank/delete/<id>', methods=['GET', 'POST'])
def song_delete(id):
	linkData = SetLink.query.join(Songs).filter_by(id=id).all()
	for link in linkData:
		db.session.delete(link)
	song = Songs.query.filter_by(id=id).first()
	db.session.delete(song)
	db.session.commit()
	return redirect(url_for('songbank'))

#define route which will bring user to form which will allow them to edit song details
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

#define route which will allow user to create a setlist in the set_list table
@app.route('/create', methods=['GET', 'POST'])
def create():
	setData = SetList.query.all()
	song = Songs.query.all()
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
	return render_template('create.html', title='Create', form=form, set_list=setData, songs=song)

#define route which will allow user to delete setlist along with any relevant data in set_link table
@app.route('/create/delete/<id>', methods=['GET', 'POST'])
def set_delete(id):
	linkData = SetLink.query.join(SetList).filter_by(id=id).all()
	for link in linkData:
		db.session.delete(link)
	setlist = SetList.query.filter_by(id=id).first()
	db.session.delete(setlist)
	db.session.commit()
	return redirect(url_for('create'))

#define route which will bring user to form which they can use to change setlist name
@app.route('/create/edit/<id>', methods=['GET', 'POST'])
def set_name_edit(id):
        set_list = SetList.query.filter_by(id=id).first()
        form = UpdateSetNameForm()
        if form.validate_on_submit():
                set_list.set_name = form.set_name.data
                db.session.commit()
                return redirect(url_for('create'))
        elif request.method == 'GET':
                form.set_name.data = set_list.set_name
        return render_template('editsetname.html', title ='Edit Set', form=form)

#defining route which will allow page to display all song and setlist data along with a form which will allow the user to enter the set id and song id which they wish to link in a setlist
@app.route('/addsetsong', methods=['GET', 'POST'])
def querysetsong():
	songData = Songs.query.all()
	setData = SetList.query.all()
	form = SongSetForm()
	if form.validate_on_submit():
		linkData = SetLink(
			fk_song_id = form.linksong.data,
			fk_setlist_id = form.linkset.data
		)
		db.session.add(linkData)
		db.session.commit()
	return render_template('addsongbank.html', title='Add to setlist', songs=songData, set_list=setData, form=form)

#defining route which will allow user to view songs from a particular setlist
@app.route('/view/<id>', methods=['GET'])
def view_song_set(id):
	songData = Songs.query.join(SetLink).filter_by(fk_setlist_id=id).all()
	return render_template('view.html', title='SetList', songs=songData)
