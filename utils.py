import os,logging
from google.appengine.api import users
def path(file_path='/'):
    return os.path.join(os.path.dirname(__file__), "templates/"+file_path )
    
def authdetails(page = "/"):
    user = users.get_current_user()
    if user: 
        label = "Sign Out"
        link = users.create_logout_url(page)
        authenticated = True
    else:
        label = "Sign In"
        link = users.create_login_url(page)
        authenticated = False
    return dict(link = link, label = label, authenticated = authenticated)
    
def authorize(role):
    def wrapper(handler_method):
        def check_login(self, *args, **kwargs):
            user = users.get_current_user()
            if not user:
                if self.request.method != 'GET':
                    self.error(403)
                else:
                    self.redirect(users.create_login_url(self.request.uri))
            elif role == "user" or (role == "admin" and users.is_current_user_admin()):
                handler_method(self, *args, **kwargs)
            else:
                if self.request.method == 'GET':
                    self.redirect("/403.html")
                else:
                    self.error(403)
        return check_login
    return wrapper

