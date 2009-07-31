import settings
from handlers import base
from google.appengine.ext import webapp
from models.company import Company

class CompanyHandler(base.CrudHandler):

    def get(self, company_url=None):
        company = Company.get_by_url(company_url)
        self.render('admin/company.html', dict(companies=Company.all(), current_company = company))

    def create(self, company_url=None):
        Company(name=self.read('name'), url=self.read('url'), description=self.read('description')).put()
        self.get()
        
    def update(self, company_url= None):
        company = Company.get_by_url(company_url)
        if company:
            company.name = self.read('name')
            company.url = self.read('url')
            company.description = self.read('description')
            company.put()
        self.redirect('/_admin/company')
        
    
    def delete(self, company_url=None):
        company = Company.get_by_url(company_url)
        if company: company.delete()
        self.get()
