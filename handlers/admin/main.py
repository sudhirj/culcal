from google.appengine.dist import use_library
use_library('django', '1.0')
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
  wsgiref.handlers.CGIHandler().run(createApp())

def createApp():
    return webapp.WSGIApplication(ROUTES, settings.DEBUG)

if __name__ == '__main__':
  main()
