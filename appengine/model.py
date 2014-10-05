
from google.appengine.ext import ndb

class User(ndb.Model):
	name = ndb.StringProperty()
	image = ndb.BlobProperty(indexed=False)
	password = ndb.StringProperty()
	is_business = ndb.BooleanProperty()
	user_type = ndb.IntegerProperty()


class Shop(ndb.Model):
	name = ndb.StringProperty()
	description = ndb.StringProperty()
	image = ndb.BlobProperty(indexed=False)
	open_time = ndb.TimeProperty()
	close_time = ndb.TimeProperty()
	pos = ndb.GeoPtProperty()

	is_24hours = ndb.BooleanProperty()
	is_hidden = ndb.BooleanProperty()
	is_deleted = ndb.BooleanProperty()

	create_time = ndb.DateTimeProperty()
	update_time = ndb.DateTimeProperty()

	star = ndb.IntegerProperty()
	score = ndb.IntegerProperty()
	review_count = ndb.IntegerProperty()
	order_count = ndb.IntegerProperty()
	
	user = ndb.KeyProperty(kind=User)


