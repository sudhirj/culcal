import wsgiref.handlers, settings, logging
from handlers import base
from google.appengine.ext import webapp
from models.city import City
from models.venue import Venue

class VenueHandler(base.CrudHandler):
  def get(self):
    self.render('admin/show.html', dict(cities = City.all()))
  
  def create(self):
    city = City.get_by_url(self.read('city'))
    if not city: raise Exception("That city doesn't exist.")
    Venue(name = self.read('name'), 
        url = self.read('url'), 
        city = city).put()
    self.get()
  
  def delete(self):
    venue = Venue.get(self.read('key'))  
    if venue : venue.delete()
    self.get()
        
    
    
    