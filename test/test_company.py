from google.appengine.ext.db import *
from models.company import Company
from models.show import Show
import extendedtestcase

class CompanyTests(extendedtestcase.ExtendedTestCase):
    
    def test_get_show_by_url(self):
        hamlet = Show(company=self.evam, name="ASLFJALIEHR3408asdTRSDF", url='hamlet')
        hamlet.put()
        self.assertEqual(hamlet.name, self.evam.get_show_by_url('hamlet').name)
