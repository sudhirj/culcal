from google.appengine.ext import db
import extendedtestcase, logging
from models.mixins import HasLocation
from helpers.staticmap import StaticMapBuilder

class Point(HasLocation):
    location = db.GeoPtProperty()

class HasLocationTests(extendedtestcase.ExtendedTestCase):
    def test_get_static_map(self):
        point = Point()
        point.location = db.GeoPt(lat = 4, lon = 5)
        self.assertEqual(StaticMapBuilder().addMarker(4.0,5.0).build(),point.get_map_url())
