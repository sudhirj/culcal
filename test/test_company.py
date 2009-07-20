from datetime import timedelta
from google.appengine.ext.db import *
from models.company import Company
from models.show import Show
import extendedtestcase

class CompanyTests(extendedtestcase.ExtendedTestCase):
    
    def test_get_show_by_url(self):
        url = self.random()
        hamlet = Show(company=self.evam, name=self.random(), url=url)
        hamlet.put()
        self.assertEqual(hamlet.name, self.evam.get_show_by_url(url).name)
    
    def test_get_new_performances_ordered_by_performance_time(self):
        perf2 = self.make_performance(self.hamlet, self.lady_andal, self.two_days_later)
        perf1 = self.make_performance(self.hamlet, self.lady_andal, self.one_day_later)
        perf_old = self.make_performance(self.hamlet, self.lady_andal, self.now - timedelta(days=3))
        perfs_from_db = self.evam.get_new_performances().fetch(100)
        self.assertEqual(2, len(perfs_from_db))
        self.assertEqual(perf1, perfs_from_db[0])
    
    def test_attempt_to_create_company_with_same_name_as_city(self):
        attempted_company = Company(name='Chennai', url='chennai')
        self.assertRaises(ValueError, attempted_company.put)
        
    def test_company_creation(self):
        company_route = '/_admin/company'
        self.admin_app.post(company_route, {'action':'create'}, status=403) # tells blank posts to bugger off 
        name = self.random()
        url = self.random()
        
        company_data = dict(action='create', name=name, url=url)
        self.admin_app.post(company_route, company_data)
        self.admin_app.post(company_route, company_data, status=403) # create the city only once
        
        company = Company.get_by_url(url)
        self.assertTrue(company)
        self.assertEqual(name, company.name)
        self.assertEqual(url, company.url)
        
    def test_company_editing(self):
        company_route = '/_admin/company'
        url = self.random()
        Company(name = self.random(), url = url, description = 'desc').put()
        
        new_name = self.random()
        new_url = self.random()
        new_desc = self.random()
        
        company_data = dict(action='update', name=new_name, url=new_url, description = new_desc)
        self.admin_app.post(company_route+'/'+url, company_data)
        company = Company.get_by_url(new_url)
        self.assertEqual(new_name, company.name)
        self.assertEqual(new_url, company.url)
        self.assertEqual(new_desc,company.description)
    
    def test_company_delete(self):
        company_route = '/_admin/company'
        url = self.random()
        Company(name = self.random(), url = url, description = 'desc').put()
        company_data = dict(action='delete')
        self.admin_app.post(company_route+'/'+url, company_data)
        self.assertFalse(Company.get_by_url(url))
        

    def test_get_route(self):
        self.assertEqual('/'+self.evam.url,self.evam.get_route())  
        
    def test_cascading_deletes(self):
        company = Company(name=self.random(), url = self.random())
        company.put()
        
        show_url = self.random()
        show = Show(name= self.random(), url = show_url, company = company)
        show.put()
        
        self.assertTrue(Show.get_by_url(show_url))
        company.delete()
        self.assertFalse(Show.get_by_url(show_url))
        
        
