import unittest
import staticmap
from staticmap import StaticMapBuilder


class TestStaticMapBuilder(unittest.TestCase):
    def testDefaults(self):
        url = StaticMapBuilder().build()
        self.assertTrue(url.startswith(staticmap.endpoint))
        self.assertTrue(url.index('&key='+staticmap.key))
        self.assertTrue(url.index('&size=300x300'))
        
    def testSingleMarker(self):
        builder = StaticMapBuilder()
        builder.addMarker(34.5, 23.6)
        self.assertTrue(builder.build().index('&markers=34.5,23.6'))
        
    def testSetSize(self):
        builder = StaticMapBuilder()
        builder.setSize(340, 532)
        self.assertTrue(builder.build().index('&size=340x532'))
    

if __name__ == '__main__':
    print
    unittest.main()
    print
    print

    
    