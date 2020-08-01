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

    def __repr__(self):
        return ''.join([
            'Song Name: ', self.song_name, ' Album: ', self.song_album, ' Artist: ', self.song_artist, ' Key: ', self.song_key, ' BPM: ', self.song_bpm
            ])

#creating setlist schema which will contain name of setlist
class SetList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    set_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return ''.join([
            'Set List Name: ', self.set_name
            ]) 

'''
#creating setlink schmea which will act as the linking table between my songs and setlist
class SetLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_song_id =  db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    fk_setlist_id =  db.Column(db.Integer, db.ForeignKey('setlist.id'), nullable=False)
'''
