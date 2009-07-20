from google.appengine.ext import db, webapp
from handlers import base
from models.city import City
from models.venue import Venue
import logging
import settings
import wsgiref.handlers

class VenueHandler(base.CrudHandler):
  def get(self):
    self.render('admin/venue.html', dict(cities=City.all()))
  
  def create(self, venue_url= None):
    city = City.get_by_url(self.read('city'))
    if not city: raise Exception("That city doesn't exist.")
    Venue(name=self.read('name'),
        url=self.read('url'),
        city=city,
        location=db.GeoPt(lat=self.read('lat'), lon = self.read('lon'))).put()
    self.get()
  
  def delete(self):
    venue = Venue.get(self.read('key'))
    if venue : venue.delete()
    self.get()
        
    
    
    
