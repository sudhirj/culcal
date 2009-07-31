#!/usr/bin/env python
import wsgiref.handlers, settings, logging
from handlers import base
from google.appengine.ext import webapp
from models.city import City

class CityHandler(base.CrudHandler):
    def get(self, city_url=None):
        current_city = City.get_by_url(city_url)
        self.render("admin/city.html", dict(cities=City.all(), current_city=current_city))
  
    def create(self, city_url=None):
        City(name=self.read('name'),
             url=self.read('url'),
             hours_offset=int(self.read('hours')),
             minutes_offset=int(self.read('minutes'))).put()
        self.get()
    
    def update(self, city_url=None):
        current_city = City.get_by_url(city_url)
        current_city.name = self.read('name')
        current_city.url = self.read('url')
        current_city.hours_offset = int(self.read('hours'))
        current_city.minutes_offset = int(self.read('minutes'))
        current_city.put()
        self.redirect('/_admin/city', False)

    def delete(self, city_url=None):
        city = City.get_by_url(city_url)
        if city: city.delete()
        self.get()
