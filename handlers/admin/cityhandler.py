#!/usr/bin/env python
import wsgiref.handlers, settings, logging
from handlers import base
from models.city import City
from google.appengine.ext import webapp

class CityHandler(base.CrudHandler):
  def get(self):
    self.render("admin/city.html", dict(cities = City.all()))
  
  def create(self):
    City(name = self.read('name')).put()
    self.get()

  def delete(self):
    city = City.get(self.read('key'))
    if city: city.delete()
    self.get()
