import unittest
from google.appengine.ext.db import *
from models.performance import Performance

class PerformanceModelTests(unittest.TestCase):
  def test_performance_creation(self):
    self.assertRaises(BadValueError,Performance,None)