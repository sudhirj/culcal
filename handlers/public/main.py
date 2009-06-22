from google.appengine.dist import use_library
use_library('django', '1.0')
from google.appengine.ext import webapp
from handlers.public.allhandlers import VenueHandler, ShowHandler, CommonHandler
import logging
import re
import settings
import wsgiref.handlers

ROUTES = [
    ('/([\w-]+)/shows/([\w-]+)/*.*', ShowHandler),
#    ('/(' + '|'.join(settings.COMPANY_URLS) + ')/([\w-]+)/*.*', CompanyHandler),
    (r'/([\w-]+)/venues/([\w-]+)/*.*', VenueHandler),
    (r'/([\w-]+)/*.*',  CommonHandler)
]

def main():
    wsgiref.handlers.CGIHandler().run(createApp())
    
def createApp():
    return webapp.WSGIApplication(ROUTES, settings.DEBUG)
    

if __name__ == '__main__':
    main()
