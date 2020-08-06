#importing database instance
from application import db


#creating song schema with name, album, artist, 
class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(100), nullable=False)
    song_album = db.Column(db.String(100), nullable=False)
    song_artist = db.Column(db.String(100), nullable=False)
    song_key = db.Column(db.String(10), nullable=False)
    song_bpm = db.Column(db.Integer, nullable=False)
    setlink2 = db.relationship('SetLink', backref=db.backref('linksong', lazy =True))

#creating setlist schema which will contain name of setlist
class SetList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    set_name = db.Column(db.String(100), nullable=False)
    setlink1 = db.relationship('SetLink', backref=db.backref('linkset', lazy =True))

#creating a SetLink schema which will facilitate my many to many relationship
class SetLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False) 
    fk_setlist_id = db.Column(db.Integer, db.ForeignKey('set_list.id'), nullable=False)
