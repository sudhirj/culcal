from datetime import timedelta
from google.appengine.ext.db import *
from models import FixedOffset,City,Performance,Venue
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
        
    def test_get_performances(self):
        Performance(show=self.hamlet, venue=self.lady_andal, utc_date_time=self.one_day_later).put()
        Performance(show=self.hamlet, venue=self.lady_andal, utc_date_time=self.three_days_later).put()
        num_matches = self.chennai.get_performances(self.two_days_later).count()
        self.assertEqual(1, num_matches)
        
        num_matches = self.chennai.get_performances(self.now).count()
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
    
    def test_smoke_city(self):
        city_route = '/'+self.chennai.url
        self.public_app.get(city_route)
        
    def test_city_updating(self):
        city_route = '/_admin/city'
        self.admin_app.post(city_route, {'action':'update'}, status=403) # tells blank posts to bugger off 
        url = self.random()
        City(name = self.random(), url = url, hours = 5, minutes = 45).put()
        
        new_name = self.random()
        new_hours = 6
        new_minutes = 34
        new_url = self.random()
        city_data = dict(action='update', name=new_name, url=new_url, hours=new_hours, minutes=new_minutes)
        self.admin_app.post(city_route+'/'+url, city_data)

        city = City.get_by_url(new_url)
        self.assertTrue(city)
        self.assertEqual(new_name, city.name)
        self.assertEqual(new_url, city.url)    
        self.assertEqual(new_hours, city.hours_offset)    
        self.assertEqual(new_minutes, city.minutes_offset)    
        
    def test_city_deletion(self):
        city_route = '/_admin/city'
        url = self.random()
        City(name = self.random(), url = url, hours = 5, minutes = 45).put()        
        city_data = dict(action='delete')
        self.admin_app.post(city_route+'/'+url, city_data)
        self.assertFalse(City.get_by_url(url))

    def test_get_route(self):
        self.assertEqual('/'+self.chennai.url,self.chennai.get_route()) 
    
    def test_cascading_delete(self):
        venue_url = self.lady_andal.url
        
        self.chennai.delete()
        self.assertFalse(Venue.get_by_url(venue_url))
        
        
        
        
        
        
        
        
        
       
        
