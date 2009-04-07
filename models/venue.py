from google.appengine.ext import db
import base
from models.city import City

class Venue(base.NamedEntity):
  city = db.ReferenceProperty(City,collection_name='venues')
