from handlers import base
from models.performance import Performance
from models.venue import Venue
from models.show import Show
import datetime

class PerformanceHandler(base.CrudHandler):
  def get(self, url = None):
    self.render('admin/performance.html', dict(performances=Performance.all(), shows=Show.all(), venues=Venue.all()))
  
  def create(self, performance=None):
    show = Show.get(self.read('show_key'))
    if not show: raise Exception("That show doesn't exist.")
    venue = Venue.get(self.read('venue_key'))
    if not venue: raise Exception("That venue doesn't exist.")
    year = int(self.read('year'))
    month = int(self.read('month'))
    day = int(self.read('day'))
    hour = int(self.read('hour'))
    minute = int(self.read('minute'))
    Performance(show = show,
                venue = venue,
                utc_date_time = datetime.datetime(year, month, day, hour, minute) - venue.city.get_timedelta()
                ).put()
    self.get()
  
  def delete(self, key = None):
    performance = Performance.get(self.read('key'))  
    if performance : performance.delete()
    self.get()
        
    
    
    
