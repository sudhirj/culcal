from google.appengine.ext import db
from show import Show
from venue import Venue
from city import City
from company import Company
import base, datetime

class Performance(base.Entity):
    show = db.ReferenceProperty(Show, collection_name='performances', required=True)
    utc_date_time = db.DateTimeProperty(required=True)
    venue = db.ReferenceProperty(Venue, collection_name='performances', required=True)
    
    cached_city = db.ReferenceProperty(City, collection_name = 'cached_performances', required = False)
    cached_company = db.ReferenceProperty(Company, collection_name = 'cached_performances', required = False)
    
    def get_local_time(self):
        return self.utc_date_time + self.venue.city.get_timedelta()
    
    def set_local_time(self, date_time):
        self.utc_date_time = date_time - self.venue.city.get_timedelta()
        
    def put(self):
        self.cached_city = self.venue.city
        self.cached_company = self.show.company
        return super(Performance, self).put()
    
    def __eq__(self,other):
        if self.is_saved(): return self.key()==other.key()
        raise Error('Not Implemented')
   
  
