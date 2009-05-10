from google.appengine.api import users
import unittest

class ExtendedTestCase(unittest.TestCase): 
  def setUp(self):
    self.temp_gcu = users.get_current_user
    self.temp_icua = users.is_current_user_admin
      
  def tearDown(self):
    users.get_current_user = self.temp_gcu
    users.is_current_user_admin = self.temp_icua

  def login(self, user="sudhir.j@gmail.com", admin=True):
    users.get_current_user = lambda user = user : users.User(user) if user else None
    if user == None: admin = False
    users.is_current_user_admin = lambda admin = admin : admin

  def logout(self):
    self.login(None)
