import settings
from handlers import base
from google.appengine.ext import webapp
from models.company import Company

class CompanyHandler(base.CrudHandler):

  def get(self, company_url=''):
    company = Company.get_by_url(company_url)
    self.render('admin/company.html', dict(companies=Company.all()))

  def create(self, company_url=''):
    Company(name=self.read('name'), url=self.read('url'), description=self.read('description')).put()
    self.get()
    
  def delete(self, company_url=''):
    company = Company.get(self.read('key'))
    if company: company.delete()
    self.get()
