from google.appengine.ext.db import *
from models.company import Company
from models.show import Show
import extendedtestcase

class ShowTests(extendedtestcase.ExtendedTestCase):
    def test_show_creation(self):
        self.assertRaises(BadValueError, Show, None)
    
    def test_show_creation_with_duplicate_url(self):
        url = self.random()
        hamlet = Show(company=self.evam, name="Hamlet spoof", url=url)
        hamlet.put()
        
        same_url_try = Show(company=self.evam, name="Hamlet other url try", url=url)
        self.assertRaises(ValueError, same_url_try.put)        
        
    def test_get_route(self):
        url = self.random()
        hamlet = Show(company=self.evam, name="Hamlet spoof", url=url)
        self.assertEqual('/' + self.evam.url + '/shows/' + hamlet.url, hamlet.get_route())
