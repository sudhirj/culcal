#!/usr/bin/env python
import wsgiref.handlers, settings

from google.appengine.ext import webapp


class MainHandler(webapp.RequestHandler):

  def get(self):
    self.response.out.write('Hello world!')


def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       settings.DEBUG)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
