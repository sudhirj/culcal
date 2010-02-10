from google.appengine.ext import db
from models.city import City
from models.mixins import HasPerformances, HasUrl, HasLocation
import base
import validators


class Venue(base.NamedEntity, HasPerformances, HasUrl, HasLocation):
    city = db.ReferenceProperty(City, collection_name='venues')
    url = db.StringProperty(required=True, validator=validators.validate_url)
    location = db.GeoPtProperty()
    
    def put(self):
        if (not self.is_saved() and self.city.get_venue_by_url(self.url)):
            raise ValueError('This URL is already being used by another venue in ' + self.city.name)
        if not self.location: self.location = db.GeoPt(lat = 0, lon=0)
        super(Venue, self).put()
    
    def get_route(self):
        return '/'+self.city.url+'/venues/'+self.url
       
    def delete(self):
        for performance in self.performances: performance.delete()
        return super(Venue, self).delete()
     