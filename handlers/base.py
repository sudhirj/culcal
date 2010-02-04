from google.appengine.ext import webapp
import cgi
import sys
import utils
import logging
import wsgiref.handlers

class CustomHandler(webapp.RequestHandler):
   
    def handle_exception(self, exception, debug_mode):
        if debug_mode: super(CustomHandler, self).handle_exception(exception, debug_mode)
        self.response.out.write(exception)
        self.response.set_status(403)
    
    def respond(self, resp):
        self.response.out.write(resp)
    
    def respond_json(self, resp):
        import simplejson
        self.response.headers["Content-Type"] = "application/json"
        self.response.out.write(simplejson.dumps(resp))
    
    def render(self, template_path, data):
        from google.appengine.ext.webapp import template
        if not data.has_key('auth'): data.update(dict(auth = utils.authdetails()))
        self.respond(template.render(utils.path(template_path), data))
    
    def read(self, name):
        return cgi.escape(self.request.get(name))
    
    
class CrudHandler(CustomHandler):
    def is_delete_request(self):
        return self.read('action') == 'delete'
        
    def post(self,data_url =""):
        action = self.read('action')
        if not action: return False
        if action == 'create': self.create(data_url)
        if action == 'update': self.update(data_url)
        if action == 'delete': self.delete(data_url)
        return True
    
  
  
