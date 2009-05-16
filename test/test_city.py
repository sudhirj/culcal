from datetime import timedelta
from google.appengine.ext.db import *
from models.city import City
from models.venue import Venue
import extendedtestcase

class CityTests(extendedtestcase.ExtendedTestCase):
    def test_city_creation_with_duplicate_urls_fails(self):
        url = self.random()
        city1 = City(name="some city", url=url)
        city1.put()
        city2 = City(name="some other city", url=url)
        self.assertRaises(ValueError, city2.put)    

    def test_basic_validations(self):
        self.assertRaises(BadValueError, City, name="city 1")
        # check bad url
        self.assertRaises(ValueError, City, name="chennai", url="chennai city")
    
    def test_get_venue_by_url(self):
        venue = Venue(city=self.chennai, name=self.random(), url=self.random())
        venue.put()
        self.assertEqual(venue.name, self.chennai.get_venue_by_url(venue.url).name)
        
        self.assertEqual(None, self.chennai.get_venue_by_url(self.random(2)))
                
    def test_get_tzinfo(self):
        self.chennai.hours_offset = 4
        self.chennai.minutes_offset = 45
        self.assertEquals(timedelta(hours=4, minutes=45), self.chennai.get_tzinfo())
        
        self.chennai.hours_offset = -4
        self.chennai.minutes_offset = -55
        self.assertEquals(timedelta(hours=-4, minutes=-55), self.chennai.get_tzinfo())
        
