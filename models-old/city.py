from datetime import timedelta
from google.appengine.ext import db
import base
from models.mixins import HasPerformances

class City(base.UrlBasedEntity, HasPerformances):
    hours_offset = db.IntegerProperty(default=0)
    minutes_offset = db.IntegerProperty(default=0)
    
    def get_venue_by_url(self, venue_url):
        return self._get_attribute_by_value(self.venues, 'url', venue_url)

    def get_timedelta(self):
        return timedelta(hours=self.hours_offset, minutes=self.minutes_offset)

    def delete(self):
        for venue in self.venues: venue.delete()
        return super(City, self).delete()