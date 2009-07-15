#!/usr/bin/env python
import wsgiref.handlers, settings, logging
from handlers import base
from google.appengine.ext import webapp
from models.city import City

class CityHandler(base.CrudHandler):
    def get(self, city = ""):
        current_city = City.get_by_url(city)
        self.render("admin/city.html", dict(cities=City.all(), current_city = current_city))
  
    def create(self, city=""):
        City(name=self.read('name'),
             url=self.read('url'),
             hours_offset=int(self.read('hours')),
             minutes_offset=int(self.read('minutes'))).put()
        self.get()

    def delete(self, city=""):
        city = City.get(self.read('key'))
        if city: city.delete()
        self.get()
