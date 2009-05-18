import wsgiref.handlers, settings, logging
from google.appengine.ext import webapp
from handlers.public.cityhandler import CityHandler

ROUTES = [
  ('/([\w-]+)', CityHandler)
]

def main():
  application = webapp.WSGIApplication(ROUTES, settings.DEBUG)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
