from google.appengine.ext.db import *
from models.performance import Performance
import extendedtestcase

class PerformanceModelTests(extendedtestcase.ExtendedTestCase):
  def test_performance_creation(self):
    self.assertRaises(BadValueError, Performance, None)
