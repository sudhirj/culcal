import unittest
from google.appengine.ext.db import *
from models.showing import Showing

class ShowingTests(unittest.TestCase):
  def test_showing_creation(self):
    self.assertRaises(BadValueError,Showing,None)