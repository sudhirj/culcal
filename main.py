from google.appengine.ext import webapp
import settings
import wsgiref.handlers


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')
 
ROUTES = [
    ('/', MainHandler)
]

def main():
    app = webapp.WSGIApplication(ROUTES, settings.DEBUG)
    wsgiref.handlers.CGIHandler().run(app)


if __name__ == '__main__':
    main()
