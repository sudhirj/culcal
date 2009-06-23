from datetime import timedelta
from google.appengine.ext.db import *
from models.base import FixedOffset
from models.city import City
from models.performance import Performance
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
        self.assertRaises(ValueError, City, name="chennai", url="chennai city") # check bad url
    
    def test_get_venue_by_url(self):
        venue = Venue(city=self.chennai, name=self.random(), url=self.random())
        venue.put()
        self.assertEqual(venue.name, self.chennai.get_venue_by_url(venue.url).name)
        
        self.assertEqual(None, self.chennai.get_venue_by_url(self.random()))
                
    def test_get_tzinfo(self):
        self.chennai.hours_offset = 4
        self.chennai.minutes_offset = 45
        self.assertEquals(timedelta(hours=4, minutes=45), self.chennai.get_timedelta())
        
    def test_get_performances_from_time(self):
        Performance(show=self.hamlet, venue=self.lady_andal, utc_date_time=self.one_day_later).put()
        Performance(show=self.hamlet, venue=self.lady_andal, utc_date_time=self.three_days_later).put()
        num_matches = self.chennai.get_performances_from_time(self.two_days_later).count()
        self.assertEqual(1, num_matches)
        
        num_matches = self.chennai.get_performances_from_time(self.now).count()
        self.assertEqual(2, num_matches)
    
    def test_city_creation(self):
        city_route = '/_admin/city'
        self.admin_app.post(city_route, {'action':'create'}, status=403) # tells blank posts to bugger off 
        name = self.random()
        url = self.random()
        
        city_data = dict(action='create', name=name, url=url, hours=5, minutes=43)
        self.admin_app.post(city_route, city_data)
        self.admin_app.post(city_route, city_data, status=403) # create the city only once
        
        city = City.get_by_url(url)
        self.assertTrue(city)
        self.assertEqual(name, city.name)
        self.assertEqual(url, city.url)

    def test_get_route(self):
        self.assertEqual('/'+self.chennai.url,self.chennai.get_route())        
        
        
        
        
        
        
        
        
        
       
        
