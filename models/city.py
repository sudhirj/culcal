from datetime import timedelta
from google.appengine.ext import db
import base


class City(base.UrlBasedEntity):
    hours_offset = db.IntegerProperty(default=0)
    minutes_offset = db.IntegerProperty(default=0)
    
    def get_venue_by_url(self, venue_url):
        matches = self.venues.filter('url =', venue_url).fetch(1)
        return matches[0] if len(matches) else None

    def get_tzinfo(self):
        return timedelta(hours=self.hours_offset, minutes=self.minutes_offset)
