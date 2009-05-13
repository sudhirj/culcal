from google.appengine.ext.db import *
from models.show import Show
from models.company import Company
import extendedtestcase

class ShowTests(extendedtestcase.ExtendedTestCase):
    def test_show_creation(self):
        self.assertRaises(BadValueError, Show, None)
    
    def test_show_creation_with_duplicate_url(self):
        hamlet = Show(company=self.evam, name="Hamlet spoof", url='hamlet')
        hamlet.put()
        
        same_url_try = Show(company=self.evam, name="Hamlet other url try", url='hamlet')
        self.assertRaises(ValueError, same_url_try.put)        
