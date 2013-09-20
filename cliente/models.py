from google.appengine.ext import db

class Cliente (db.Model):
	name = db.StringProperty()

	