import extendedtestcase
from google.appengine.ext.db import *
from models.city import City

class CityTests(extendedtestcase.ExtendedTestCase):
  def test_city_creation_with_duplicate_urls_fails(self):
    city1 = City(name ="Chennai", url="chennai")
    city1.put()
    city2 = City(name = "Chennai2", url = "chennai")
    self.assertRaises(ValueError,city2.put)

  def test_basic_validations(self):
    self.assertRaises(BadValueError,City, name = "city 1")
    self.assertRaises(ValueError, City, name ="chennai", url = "chennai city")
    