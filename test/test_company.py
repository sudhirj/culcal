from google.appengine.ext.db import *
from models.company import Company
from models.show import Show
import extendedtestcase
from datetime import timedelta

class CompanyTests(extendedtestcase.ExtendedTestCase):
    
    def test_get_show_by_url(self):
        url = self.random()
        hamlet = Show(company=self.evam, name=self.random(2), url=url)
        hamlet.put()
        self.assertEqual(hamlet.name, self.evam.get_show_by_url(url).name)
    
    def test_get_new_performances_ordered_by_performance_time(self):
        perf2 = self.make_performance(self.hamlet, self.lady_andal, self.two_days_later)
        perf1 = self.make_performance(self.hamlet, self.lady_andal, self.one_day_later)
        perf_old = self.make_performance(self.hamlet, self.lady_andal, self.now - timedelta(days = 3))
        perfs_from_db =self.evam.get_new_performances().fetch(100)
        self.assertEqual(2, len(perfs_from_db))
        self.assertEqual(perf1, perfs_from_db[0])
    
    def test_attempt_to_create_company_with_same_name_as_city(self):
        attempted_company = Company(name ='Chennai', url = 'chennai')
        self.assertRaises(ValueError,attempted_company.put)
        
        
        
        
