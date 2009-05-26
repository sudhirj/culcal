import wsgiref.handlers, settings, logging, re
from google.appengine.ext import webapp
from handlers.public.cityhandler import CityHandler, CompanyHandler

ROUTES = [
    ('/('+'|'.join(settings.COMPANY_URLS)+')/([\w-]+)',CompanyHandler),
    (r'/([\w-]+)', CityHandler)
]

def main():
  application = webapp.WSGIApplication(ROUTES, settings.DEBUG)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
