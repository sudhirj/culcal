#!/usr/bin/env python
import wsgiref.handlers, settings, logging
from google.appengine.ext import webapp
from handlers.admin import cityhandler

ROUTES = [
  ('/_admin/city', cityhandler.CityHandler)
]

def main():
  application = webapp.WSGIApplication(ROUTES, settings.DEBUG)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
