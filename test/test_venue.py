from google.appengine.ext.db import *
from models.venue import Venue
from models.city import City
import extendedtestcase, logging

class VenueTests(extendedtestcase.ExtendedTestCase):
      
    def test_venue_creation_with_duplicate_url(self):
        url = self.random();
        venue = Venue(name=self.random(2), url=url, city=self.chennai)
        venue.put()
        venue_with_duplicate_url = Venue(city=self.chennai, name=self.random(3), url=url)
        self.assertRaises(ValueError, venue_with_duplicate_url.put)    
         
