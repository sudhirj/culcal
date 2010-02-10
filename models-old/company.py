import base, datetime
from models.mixins import HasPerformances
from models.city import City
from google.appengine.ext import db

class Company(base.UrlBasedEntity, HasPerformances):
    description = db.TextProperty(required = False, default = "")
    
    def get_show_by_url(self, show_url):
        return self._get_attribute_by_value(self.shows, 'url', show_url)

    def put(self):
        if City.get_by_url(self.url): raise ValueError('This url is being used by a city')
        return super(Company, self).put()
        
    def delete(self):
        for show in self.shows: show.delete()
        return super(Company, self).delete()