import wsgiref.handlers, settings, logging
from handlers import base
from google.appengine.ext import webapp
from models.show import Show
from models.company import Company

class ShowHandler(base.CrudHandler):
  def get(self):
    self.render('admin/show.html', dict(shows = Show.all(), companies = Company.all()))
  
  def create(self):
    company = Company.get_by_url(self.read('company'))
    if not company: raise Exception("That company doesn't exist.")
    Show(name = self.read('name'), 
        url = self.read('url'), 
        company = company).put()
    self.get()
  
  def delete(self):
    show = Show.get(self.read('key'))  
    if show : show.delete()
    self.get()
        
    
    
    