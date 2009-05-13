from google.appengine.ext import db
import base

class City(base.UrlBasedEntity):
    
    def get_venue_by_url(self, venue_url):
        matches = self.venues.filter('url =', venue_url).fetch(1)
        return matches[0] if len(matches) else None

 
  
