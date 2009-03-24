#!/usr/bin/env python
import wsgiref.handlers, settings, logging
from handlers import basehandler
from models.city import City
from google.appengine.ext import webapp

class CityHandler(basehandler.CustomHandler):

  def get(self):
    self.render("admin/city.html",  dict(cities=City.all()))
  
  def post(self):
    if self.is_delete_request():
      self.delete(self.read_param('key'))
      self.get()
      return
    city = City(name=self.read_param('name'))
    city.put()
    self.get()

  def delete(self, key):
    city = City.get(key)
    if city: city.delete()