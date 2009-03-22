from google.appengine.ext import db


class Entity(db.Model):
  created_at = db.DateTimeProperty(auto_now_add = True)
  updated_at = db.DateTimeProperty(auto_now = True)
  
class NamedEntity(Entity):
  name = db.StringProperty(required = True)
  

      
      