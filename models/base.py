from datetime import timedelta, tzinfo
from google.appengine.ext import db
import re
import settings
import validators
from mixins import HasUrl

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

    @property
    def str(self):
        return self.name.upper().strip().replace(' ','')
    
    
  
class UrlBasedEntity(NamedEntity, HasUrl):
    url = db.StringProperty(required=True, validator=validators.validate_url)
    def put(self):
        if (not self.is_saved()) and self.get_by_url(self.url):
            raise ValueError("This URL is already in use.")
        super(UrlBasedEntity, self).put()

    def get_route(self):
        return '/'+self.url
        

class FixedOffset(tzinfo):
    def __init__(self, offset):
        self.__offset = offset

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return "FixedOffset:" + self._offset 

    def dst(self, dt):
        return None
    
    def __eq__(self, other):
        return self.__offset == other.__offset
      
      
