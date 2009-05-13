import wsgiref.handlers, utils, cgi, traceback, sys

from google.appengine.ext import webapp


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
        self.respond(template.render(utils.path(template_path), data))
    
    def read(self, name):
        return cgi.escape(self.request.get(name))
    
    def is_delete_request(self):
        return self.read('action') == 'delete'
    
class CrudHandler(CustomHandler):
    def post(self):
        action = self.read('action')
        if not action: return False
        if action == 'create': self.create()
        if action == 'update': self.update()
        if action == 'delete': self.delete()
        return True
    
  
  
