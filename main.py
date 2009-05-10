#!/usr/bin/env python
from google.appengine.ext import webapp
import wsgiref.handlers
import settings


class MainHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write('Hello world!')
 
ROUTES = [
  ('/', MainHandler)
]

def main():
  application = webapp.WSGIApplication(ROUTES, settings.DEBUG)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
