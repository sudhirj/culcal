from google.appengine.ext import db, webapp
from handlers import base
from models.city import City
from models.venue import Venue
import logging
import settings
import wsgiref.handlers

class VenueHandler(base.CrudHandler):
    def get(self, venue_url = None):
        self.render('admin/venue.html', dict(cities=City.all(), current_venue = Venue.get_by_url(venue_url)))
  
    def create(self, venue_url= None):
        city = self.check_city()
        Venue(name=self.read('name'),
            url=self.read('url'),
            city=city,
            location=db.GeoPt(lat=self.read('lat'), lon = self.read('lon'))).put()
        self.get()
    
    def update(self, venue_url = None):
        venue = Venue.get_by_url(venue_url)
        if not venue: raise Exception("That venue doesn't exist")
        venue.name=self.read('name')
        venue.url=self.read('url')
        venue.city=self.check_city()
        venue.location=db.GeoPt(lat=self.read('lat'), lon = self.read('lon'))
        venue.put()
        self.redirect('/_admin/venue/')
        
    def check_city(self):
        city = City.get_by_url(self.read('city'))
        if not city: raise Exception("That city doesn't exist.")
        return city
        
  
    def delete(self, venue_url= None):
        venue = Venue.get_by_url(venue_url)
        if venue : venue.delete()
        self.get()
        
    
    
    
