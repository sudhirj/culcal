#!/usr/bin/env python
import wsgiref.handlers, settings, logging
from google.appengine.ext import webapp
from handlers.admin import cityhandler, companyhandler, showhandler, venuehandler, performancehandler


ROUTES = [
  ('/_admin/city', cityhandler.CityHandler),
  ('/_admin/show', showhandler.ShowHandler),
  ('/_admin/company', companyhandler.CompanyHandler),
  ('/_admin/venue', venuehandler.VenueHandler),
  ('/_admin/performance', performancehandler.PerformanceHandler)
]

def main():
  application = webapp.WSGIApplication(ROUTES, settings.DEBUG)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
