from google.appengine.ext import db

class NamedEntity(db.Model):
  name = db.StringProperty(required = True)
  datetime = db.DateTimeProperty(auto_now_add = True)