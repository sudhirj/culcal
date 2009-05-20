from datetime import timedelta
from google.appengine.ext import db
import base


class City(base.UrlBasedEntity):
    hours_offset = db.IntegerProperty(default=0)
    minutes_offset = db.IntegerProperty(default=0)
    
    def get_venue_by_url(self, venue_url):
        return self._get_attribute_by_value(self.venues, 'url', venue_url)

    def get_timedelta(self):
        return timedelta(hours=self.hours_offset, minutes=self.minutes_offset)
    
    def get_performances_from_time(self, dt):
        return self.cached_performances.filter('utc_date_time >', dt).order('utc_date_time')