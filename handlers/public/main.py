import wsgiref.handlers, settings, logging, re
from google.appengine.ext import webapp
from handlers.public.allhandlers import CityHandler, CompanyHandler, VenueHandler, ShowHandler

ROUTES = [
    ('/(' + '|'.join(settings.COMPANY_URLS) + ')/([\w-]+)/shows/([\w-]+)/*.*', ShowHandler),
    ('/(' + '|'.join(settings.COMPANY_URLS) + ')/([\w-]+)/*.*', CompanyHandler),
    (r'/([\w-]+)/venues/([\w-]+)/*.*', VenueHandler),
    (r'/([\w-]+)/*.*', CityHandler)
]

def main():
  application = webapp.WSGIApplication(ROUTES, settings.DEBUG)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
