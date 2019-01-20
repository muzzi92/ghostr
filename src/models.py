from google.appengine.ext import ndb


class Ghost(ndb.Model):
    gmail = ndb.UserProperty()
    ghost_name = ndb.StringProperty()
    first_name = ndb.StringProperty()
    second_name = ndb.StringProperty()
