import wsgiref.handlers, settings, logging
from handlers import base
from google.appengine.ext import webapp
from models.show import Show
from models.company import Company

class ShowHandler(base.CrudHandler):
    def get(self, show_url = None):
        show = Show.get_by_url(show_url)
        self.render('admin/show.html', dict(shows = Show.all(), companies = Company.all(), current_show = show))
  
    def create(self, show_url = None):
        company = self.check_company()
        Show(name = self.read('name'), 
            url = self.read('url'), 
            company = company,
            description = self.read('desc')).put()
        self.get()
        
    def update(self, show_url=None):
        show = Show.get_by_url(show_url)
        if not show: raise Exception("Show doesn't exist")
        show.name = self.read('name')
        show.url = self.read('url') 
        show.company = self.check_company()
        show.description = self.read('desc')
        show.put()
        self.redirect('/_admin/show/')
        
        
        
    def delete(self, show_url = None):
        show = Show.get_by_url(show_url) 
        if show : show.delete()
        self.get()
    
    def check_company(self):
        company = Company.get_by_url(self.read('company'))
        if not company: raise Exception("That company doesn't exist.")
        return company
        
    
    
    