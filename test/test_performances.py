from google.appengine.ext import db
from models.performance import Performance
import datetime
import extendedtestcase
import logging

class PerformanceModelTests(extendedtestcase.ExtendedTestCase):
    def test_performance_creation(self):
        self.assertRaises(db.BadValueError, Performance, None)
        
    def test_local_time(self):
        self.chennai.hours_offset = 5
        self.chennai.minutes_offset = 30 
        self.chennai.put()
        
        now = datetime.datetime.now()
        perf = Performance(show=self.hamlet, venue=self.lady_andal, utc_date_time=now)
        self.assertEqual(now + self.chennai.get_timedelta(), perf.get_local_time())
        
        perf.set_local_time(now + self.chennai.get_timedelta())
        self.assertEqual(now, perf.utc_date_time)
        self.assertEqual(now + self.chennai.get_timedelta(), perf.get_local_time())
    
    def test_cache(self):
        now = datetime.datetime.now()
        perf = Performance(show=self.hamlet, venue=self.lady_andal, utc_date_time=now)
        perf.put()
        self.assertEqual(self.chennai, perf.cached_city)
        self.assertEqual(self.evam, perf.cached_company)

    def test_company_performance(self):
        performance_route = '/_admin/performance'
        self.admin_app.post(performance_route, {'action':'create'}, status=403) # tells blank posts to bugger off 
        old_count = self.lady_andal.get_new_performances().count()
        name = self.random()
        url = self.random()
        performance_data = dict(action='create',
                                show_key=self.hamlet.key(),
                                venue_key=self.lady_andal.key(),
                                year=self.two_days_later.date().year,
                                month=self.two_days_later.date().month,
                                day=self.two_days_later.date().day,
                                hour=self.two_days_later.time().hour,
                                minute=self.two_days_later.time().minute)
        self.admin_app.post(performance_route, performance_data)
        
        self.assertEqual(old_count + 1, self.lady_andal.get_new_performances().count())
        result = Performance.all().filter('show =', self.hamlet).filter('venue =', self.lady_andal).filter('utc_date_time =', self.two_days_later).fetch(1)[0]
        self.assertTrue(result)
        
