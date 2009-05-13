from google.appengine.ext import db
from models.performance import Performance
import extendedtestcase


class PerformanceModelTests(extendedtestcase.ExtendedTestCase):
    def test_performance_creation(self):
        self.assertRaises(db.BadValueError, Performance, None)
        
        
