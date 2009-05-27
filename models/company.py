import base, datetime
from models.city import City
from google.appengine.ext import db

class Company(base.UrlBasedEntity):
    description = db.TextProperty(required = False, default = "")
    
    def get_show_by_url(self, show_url):
        return self._get_attribute_by_value(self.shows, 'url', show_url)
    
    def get_new_performances(self):
        return self.cached_performances.filter('utc_date_time >' ,datetime.datetime.now()).order('utc_date_time')
    
    def put(self):
        if City.get_by_url(self.url): raise ValueError('This url is being used by a city')
        return super(Company, self).put()