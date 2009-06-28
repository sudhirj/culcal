from google.appengine.ext.db import *
from models.company import Company
from models.show import Show
from models.performance import Performance
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
        
    def test_get_by_url(self):
        url = self.random()
        Show(company= self.evam, name ="new show", url = url, desc = "lorem ipsum dolor").put()
        show = Show.get_by_url(url)
        self.assertEqual(show.name,"new show")
        

    def test_show_creation_by_admin(self):
        show_route = '/_admin/show'
        self.admin_app.post(show_route, {'action':'create'}, status=403) # tells blank posts to bugger off 
        name = self.random()
        url = self.random()
        description = self.random()
        company = self.evam.url

        show_data = dict(action='create', name=name, url=url, desc = description, company = company)
        self.admin_app.post(show_route, show_data)
        self.admin_app.post(show_route, show_data, status=403) # create the show only once

        show = Show.get_by_url(url)
        self.assertTrue(show)
        self.assertEqual(name, show.name)
        self.assertEqual(url, show.url)
        self.assertEqual(description, show.desc)
        
    def test_cascading_deletes(self):
        self.make_performance(self.hamlet, self.lady_andal, self.one_day_later)
        self.make_performance(self.hamlet, self.lady_andal, self.two_days_later)
        perf_count = Performance.all().count()
        self.hamlet.delete()
        self.assertEqual(perf_count-2,Performance.all().count())
        
        
        
        