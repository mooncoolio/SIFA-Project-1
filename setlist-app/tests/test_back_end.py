import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Songs, SetList, SetLink
from os import getenv

class TestBase(TestCase):

	def create_app(self):
		config_name = 'testing'
		app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
			SECRET_KEY=getenv('TEST_SECRET_KEY'),
			WTF_CSRF_ENABLED=False,
			DEBUG=True
			)
		return app

	def setUp(self):
		db.session.commit()
		db.drop_all()
		db.create_all()
		song = Songs(song_name= "Test", song_album="Test", song_artist="Test", song_key="C", song_bpm="125")
		db.session.add(song)
		db.session.commit()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

#Testing that home page can be accessed
class TestViews(TestBase):

	def test_home_view(self):
		response = self.client.get(url_for('home'))
		self.assertEqual(response.status_code, 200)

#Testing that songbank will enter test variables into system and return user to songbank with test varaibles populated
class TestAddSongBank(TestBase):

	def test_add_song_bank(self):
		with self.client:
			response = self.client.post(
				'/addsong',
				data=dict(
					song_name = "Test1",
					song_album = "Test1",
					song_artist = "Test1",
					song_key = "C",
					song_bpm = "125"
				),
				follow_redirects=True
		)
		self.assertIn(b'Test1', response.data)
	#Testing that redirect will not happen when a letter is put into our bpm integer field
	def test_add_song_error(self):
		with self.client:
			response = self.client.post(
				'/addsong',
				data=dict(
					song_name = "Test1",
					song_album = "Test1",
					song_artist = "Test1",
					song_key = "C",
					song_bpm = "C"
				),
				follow_redirects=False
		)
		self.assertIn(b'Add songs', response.data)

#Testing that songbank will return test varaibles from set up method
class TestSongBank(TestBase):

	def test_song_bank(self):
		response = self.client.get(url_for('songbank'))
		self.assertIn(b'Test', response.data)

class TestSongDelete(TestBase):
	
	def test_song_delete(self):
		response = self.client.get(url_for('song_delete', id=1))
		self.assertNotIn(b'Test', response.data)


class TestSongEdit(TestBase):
	def test_song_edit(self):
		response = self.client.get(url_for('song_edit', id=1))
		self.assertIn(b'Edit Song Details', response.data)

	def test_song_edit_1(self):
		with self.client:
			response = self.client.post('song_edit',
			data=dict(
				song_name = "Tost1",
				song_album = "Tost1",
				song_artist = "Tost1",
				song_key = "C",
				song_bpm = "125"
			),
			follow_redirects=True
		)
		self.assertNotIn(b'Test', response.data)

class TestSetCreate(TestBase):

	def test_set_create(self):
		response = self.client.post(
			'/create',
			data=dict(
				set_name= "TestingTestTest"
			),
			follow_redirects=True
		)
		self.assertIn(b'TestingTestTest', response.data)
