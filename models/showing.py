from google.appengine.ext import db
from show import Show
import base_models

class Showing(base_models.Entity):
  show = db.ReferenceProperty(Show,collection_name='showings', required = True)
  time = db.DateTimeProperty(required = True)
  
