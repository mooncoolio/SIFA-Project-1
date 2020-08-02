from flask_table import Table, Col

class SongTable(Table):
	id = Col('ID' show=False)
	song_name = ('Song Name')
	song_album = ('Album')
	song_artist = ('Artist')
	song_key = ('Key')
	song_bpm = ('BPM')
