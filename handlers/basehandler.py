import wsgiref.handlers, utils, cgi

from google.appengine.ext import webapp


class CustomHandler(webapp.RequestHandler):
  def handle_exception(self,exception, debug_mode):
    self.response.out.write(exception)
    self.response.set_status(403)
  def respond(self,resp):
    self.response.out.write(resp)
  def respond_json(self, resp):
    import simplejson
    self.response.headers["Content-Type"] = "application/json"
    self.response.out.write(simplejson.dumps(resp))
  def render(self, template_path, data):
    from google.appengine.ext.webapp import template
    self.respond(template.render(utils.path(template_path),data))
  def read_param(self,name):
    return cgi.escape(self.request.get(name))
  def is_delete_request(self):
    return self.read_param('action') == 'delete'
