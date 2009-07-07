import unittest, settings
import helpers.staticmap as staticmap
from helpers.staticmap import StaticMapBuilder

class TestStaticMapBuilder(unittest.TestCase):
    def testDefaults(self):
        url = StaticMapBuilder().build()
        self.assertTrue(url.startswith(settings.MAP_ENDPOINT))
        self.assertTrue(url.index('&key='+settings.MAP_KEY))
        self.assertTrue(url.index('&size='+str(settings.MAP_SIZE['x'])+'x'+str(settings.MAP_SIZE['y'])))
        
    def testSingleMarker(self):
        builder = StaticMapBuilder()
        builder.addMarker(34.5, 23.6)
        self.assertTrue(builder.build().index('&markers=34.5,23.6'))
