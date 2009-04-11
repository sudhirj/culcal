from google.appengine.ext import db
import re, settings

class Entity(db.Model):
  created_at = db.DateTimeProperty(auto_now_add = True)
  updated_at = db.DateTimeProperty(auto_now = True)
  
class NamedEntity(Entity):
  
  def validate_name(string):
    if string == None or string.isspace() : raise ValueError("Name can't be blank")

  name = db.StringProperty(required = True, validator = validate_name)
  
class UrlBasedEntity(NamedEntity):
  
  def validate_url(url):
    if re.search(settings.URL_VALIDATOR, url): raise ValueError("The URL contains invalid characters - only alphanumerics and hyphens allowed.")
  url = db.StringProperty(required = True, validator = validate_url )
  
  @classmethod
  def get_by_url(cls, url):
    matches = cls.all().filter('url =', url).fetch(1)  
    return matches[0] if len(matches) else None
    
  
  def put(self):
    if (not self.is_saved()) and self.get_by_url(self.url):
      raise ValueError("This URL is already in use.")
    super(NamedEntity, self).put()

      
      
