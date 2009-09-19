from google.appengine.dist import use_library
use_library('django', '1.0')
from google.appengine.ext import webapp
from handlers.public.allhandlers import VenueHandler, ShowHandler, CommonHandler, HomepageHandler, SearchHandler
import logging
import re
import settings
import wsgiref.handlers

ROUTES = [
    (r'/search/*', SearchHandler),
    (r'/([\w-]+)/shows/([\w-]+)/*.*', ShowHandler),
    (r'/([\w-]+)/venues/([\w-]+)/*.*', VenueHandler),
    (r'/([\w-]+)/*.*',  CommonHandler),
    (r'.*', HomepageHandler)
]

def main():
    wsgiref.handlers.CGIHandler().run(createApp())
    
def createApp():
    return webapp.WSGIApplication(ROUTES, settings.DEBUG)

        

if __name__ == '__main__':
    main()
