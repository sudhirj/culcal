from google.appengine.ext import db
from show import Show
from venue import Venue
import base

class Performance(base.Entity):
    show = db.ReferenceProperty(Show, collection_name='performances', required=True)
    utc_date_time = db.DateTimeProperty(required=True)
    venue = db.ReferenceProperty(Venue, collection_name='shows', required=True)
    
    def get_local_time(self):
        return self.utc_date_time + self.venue.city.get_timedelta()
    
    def set_local_time(self, date_time):
        self.utc_date_time = date_time - self.venue.city.get_timedelta()
        
   
  
