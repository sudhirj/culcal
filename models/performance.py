from google.appengine.ext import db
from show import Show
from venue import Venue
import base

class Performance(base.Entity):
    show = db.ReferenceProperty(Show, collection_name='performances', required=True)
    date_time = db.DateTimeProperty(required=True)
    venue = db.ReferenceProperty(Venue, collection_name='shows', required=True)


  
