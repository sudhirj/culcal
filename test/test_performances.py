from google.appengine.ext import db
from models.performance import Performance
import datetime
import extendedtestcase

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
    
        
        
        
        
        
        
