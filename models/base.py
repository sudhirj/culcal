from google.appengine.ext import db

class Entity(db.Model):
  created_at = db.DateTimeProperty(auto_now_add = True)
  updated_at = db.DateTimeProperty(auto_now = True)
  
class NamedEntity(Entity):
  
  def validate_name(string):
    if string == None or string.isspace() : raise ValueError("Name can't be blank")

  name = db.StringProperty(required = True, validator = validate_name)
  
  

      
      
