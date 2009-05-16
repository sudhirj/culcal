from datetime import timedelta, tzinfo
from google.appengine.ext import db
import re
import settings
import validators

class Entity(db.Model):
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)
    
    @staticmethod
    def _get_attribute_by_value(attribute, filter_property, value):
        matches = attribute.filter(filter_property + ' =', value).fetch(1)
        return matches[0] if len(matches) else None
        
  
class NamedEntity(Entity):
  
    def validate_name(string):
        if string == None or string.isspace() : raise ValueError("Name can't be blank")

    name = db.StringProperty(required=True, validator=validate_name)
    
    
  
class UrlBasedEntity(NamedEntity):
  
    url = db.StringProperty(required=True, validator=validators.validate_url)
  
    @classmethod
    def get_by_url(cls, url):
        return cls._get_attribute_by_value(cls.all(), 'url', url)
  
    def put(self):
        if (not self.is_saved()) and self.get_by_url(self.url):
            raise ValueError("This URL is already in use.")
        super(NamedEntity, self).put()


class FixedOffset(tzinfo):
    def __init__(self, hours=0, minutes=0):
        self.__offset = timedelta(hours=hours, minutes=minutes)

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return "FixedOffset:" + self._offset 

    def dst(self, dt):
        return ZERO
      
      
