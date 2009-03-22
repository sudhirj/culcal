#!/usr/bin/env python
import wsgiref.handlers, settings, logging
from handlers import base_handler
from models.city import City
from google.appengine.ext import webapp



class CityHandler(base_handler.CustomHandler):

  def get(self):
    self.render("admin/city.html",  dict(cities=City.all()))
    logging.info(City.all())
  
  def post(self):
    if self.read_param('action') == 'delete':
      self.delete(self.read_param('key'))
      self.get()
      return
    city = City(name=self.read_param("city_name"))
    city.put()
    self.get()

  def delete(self, key):
    city = City.get(key)
    city.delete()

ROUTES = [
  ('/_admin/city', CityHandler)
]

def main():
  application = webapp.WSGIApplication(ROUTES, settings.DEBUG)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
