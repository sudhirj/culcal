from google.appengine.ext.db import *
from models.company import Company
from models.show import Show
import extendedtestcase

class CompanyTests(extendedtestcase.ExtendedTestCase):
    
    def test_get_show_by_url(self):
        url = self.random()
        hamlet = Show(company=self.evam, name=self.random(2), url=url)
        hamlet.put()
        self.assertEqual(hamlet.name, self.evam.get_show_by_url(url).name)
