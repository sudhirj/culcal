from google.appengine.ext import db
import basemodels
from models.city import City

class Venue(basemodels.NamedEntity):
  city = db.ReferenceProperty(City,collection_name='venues')
