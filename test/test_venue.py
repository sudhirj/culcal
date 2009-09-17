from google.appengine.ext.db import *
from models.venue import Venue
from models.performance import Performance
from models.city import City
import extendedtestcase, logging
from google.appengine.ext import db


class VenueTests(extendedtestcase.ExtendedTestCase):
      
    venue_route = '/_admin/venue/'  
    def test_venue_creation_with_duplicate_url(self):
        url = self.random();
        venue = Venue(name=self.random(), url=url, city=self.chennai)
        venue.put()
        venue_with_duplicate_url = Venue(city=self.chennai, name=self.random(), url=url)
        self.assertRaises(ValueError, venue_with_duplicate_url.put)    
         
    def test_perf_mixin_inherit(self):
        from models.mixins import HasPerformances, HasLocation
        self.assertTrue(issubclass(Venue, HasPerformances))
        self.assertTrue(issubclass(Venue, HasLocation))
        self.assertTrue(hasattr(self.lady_andal, 'location'))
        self.assertTrue(hasattr(self.lady_andal, 'performances'))
        
    def test_get_route(self):
        url = self.random();
        venue = Venue(name=self.random(), url=url, city=self.chennai)
        self.assertEqual('/'+self.chennai.url+'/venues/'+venue.url,venue.get_route())

    def test_cascading_deletes(self):
        self.make_performance(self.hamlet, self.lady_andal, self.one_day_later)
        self.make_performance(self.hamlet, self.lady_andal, self.two_days_later)
        perf_count = Performance.all().count()
        self.lady_andal.delete()
        self.assertEqual(perf_count-2,Performance.all().count())
        
    def test_venue_creation_by_admin(self):
        name = self.random()
        url = self.random()
        lat = 4
        lon = 5
        venue_data = dict(name = name, url = url, lat = lat, lon = lon, action='create', city = self.chennai.url)
        self.admin_app.post(self.venue_route, venue_data)
        venue = Venue.get_by_url(url)
        self.assertTrue(venue)
        self.assertEqual(name,venue.name)
        self.assertEqual(lat,venue.location.lat)
        self.assertEqual(lon,venue.location.lon)
        self.assertEqual(self.chennai.url,venue.city.url)
        
    def test_venue_edit_by_admin(self):
        name = self.random()
        url = self.random()
        lat = 4
        lon = 5
        Venue(name = self.random(), url = url, city = self.chennai, location = db.GeoPt(lat = 0, lon = 0)).put()
        new_url = self.random()
        venue_data = dict(name = name, url = new_url, lat = lat, lon = lon, action='update', city = self.bangalore.url)
        self.admin_app.post(self.venue_route+url, venue_data)
        venue = Venue.get_by_url(new_url)
        self.assertTrue(venue)
        self.assertEqual(name,venue.name)
        self.assertEqual(lat,venue.location.lat)
        self.assertEqual(lon,venue.location.lon)
        self.assertEqual(self.bangalore.url,venue.city.url)
        
    def test_delete_by_admin(self):
        url = self.random()
        Venue(name = self.random(), url = url, city = self.chennai, location = db.GeoPt(lat = 0, lon = 0)).put()
        self.assertTrue(Venue.get_by_url(url))
        venue_data = dict(action ='delete')
        self.admin_app.post(self.venue_route+url, venue_data)
        self.assertFalse(Venue.get_by_url(url))
        
    def test_smoke_venue(self):
        self.public_app.get("/"+self.lady_andal.city.url+"/"+self.lady_andal.url)
        
        

        
        
        
        
        
        
        
        
        
        