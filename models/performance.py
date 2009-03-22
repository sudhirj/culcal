from google.appengine.ext import db
from show import Show
from venue import Venue
import base_models

class Performance(base_models.Entity):
  show = db.ReferenceProperty(Show,collection_name='performances', required = True)
  datetime = db.DateTimeProperty(required = True)
  venue = db.ReferenceProperty(Venue,collection_name='shows', required = True)


  
