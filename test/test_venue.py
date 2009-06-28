from google.appengine.ext.db import *
from models.venue import Venue
from models.performance import Performance
from models.city import City
import extendedtestcase, logging


class VenueTests(extendedtestcase.ExtendedTestCase):
      
    def test_venue_creation_with_duplicate_url(self):
        url = self.random();
        venue = Venue(name=self.random(), url=url, city=self.chennai)
        venue.put()
        venue_with_duplicate_url = Venue(city=self.chennai, name=self.random(), url=url)
        self.assertRaises(ValueError, venue_with_duplicate_url.put)    
         
    def test_perf_mixin_inherit(self):
        from models.mixins import HasPerformances
        self.assertTrue(issubclass(Venue, HasPerformances))
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