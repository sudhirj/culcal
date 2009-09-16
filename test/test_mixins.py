from google.appengine.ext import db
import extendedtestcase, logging
from models.mixins import HasLocation
from models.city import City
from helpers.staticmap import StaticMapBuilder

class Point(HasLocation):
    location = db.GeoPtProperty()

class HasLocationTests(extendedtestcase.ExtendedTestCase):
    def test_get_static_map(self):
        point = Point()
        point.location = db.GeoPt(lat=4, lon=5)
        self.assertEqual(StaticMapBuilder().addMarker(4.0, 5.0).build(), point.get_map_url())


class HasPerformancesTest(extendedtestcase.ExtendedTestCase):
    def test_get_new_performances_with_start_point(self):
        perf1 = self.make_performance(self.hamlet,self.lady_andal,self.one_day_later)
        perf2 = self.make_performance(self.hamlet,self.lady_andal,self.two_days_later)
        perf3 = self.make_performance(self.hamlet,self.lady_andal,self.three_days_later)
        
        self.assertEqual(3,len(self.hamlet.get_new_performances().fetch(100)))
        self.assertEqual(2,len(self.hamlet.get_new_performances(start_after=perf1.time_sort).fetch(100)))
        self.assertEqual(1,len(self.hamlet.get_new_performances(start_after=perf2.time_sort).fetch(100)))
   