from google.appengine.ext import db
from models.city import City
import base, validators

class Venue(base.NamedEntity):
  city = db.ReferenceProperty(City, collection_name='venues')
  url = db.StringProperty(required = True, validator = validators.validate_url)
