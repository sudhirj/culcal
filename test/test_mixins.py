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
        perf3 = self.make_performance(self.hamlet,self.lady_andal,self.three_days_later)
        perf2 = self.make_performance(self.hamlet,self.lady_andal,self.two_days_later)
        perf1 = self.make_performance(self.hamlet,self.lady_andal,self.one_day_later)

        first_page = self.hamlet.get_new_performances().fetch(100)
        self.assertEqual(3,len(first_page))
        self.assertTrue(first_page.index(perf1) < first_page.index(perf2) < first_page.index(perf3))
        
        second_page = self.hamlet.get_new_performances(start_after=perf1.time_sort).fetch(100)
        self.assertEqual(2,len(second_page))
        self.assertTrue(second_page.index(perf2) < second_page.index(perf3))
        
        last_page = self.hamlet.get_new_performances(start_after=perf2.time_sort).fetch(100)
        self.assertEqual(1,len(last_page))
        last_page.index(perf3)
   