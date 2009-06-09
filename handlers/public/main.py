from google.appengine.ext import webapp
from handlers.public.allhandlers import CityHandler, CompanyHandler, VenueHandler, ShowHandler
import logging
import re
import settings
import wsgiref.handlers

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
