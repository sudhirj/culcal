from google.appengine.ext import db
import base_models
from models.city import City

class Venue(base_models.NamedEntity):
  city = db.ReferenceProperty(City,collection_name='venues')
