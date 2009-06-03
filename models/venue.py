from google.appengine.ext import db
from models.city import City
from models.mixins import HasPerformances
import base
import validators


class Venue(base.NamedEntity, HasPerformances):
    city = db.ReferenceProperty(City, collection_name='venues')
    url = db.StringProperty(required=True, validator=validators.validate_url)
    
    def put(self):
        if (not self.is_saved() and self.city.get_venue_by_url(self.url)):
            raise ValueError('This URL is already being used by another venue in ' + self.city.name)
        super(Venue, self).put()
