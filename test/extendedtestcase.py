from google.appengine.api import users
import unittest
from models.company import Company
from models.city import City

class ExtendedTestCase(unittest.TestCase): 
    def random(self, salt=1):
        import hashlib, time
        return hashlib.md5((time.clock()*salt).__str__()).hexdigest()
    
    def setUp(self):
        self.temp_gcu = users.get_current_user
        self.temp_icua = users.is_current_user_admin
        
        self.make_test_data()
      
    def tearDown(self):
        users.get_current_user = self.temp_gcu
        users.is_current_user_admin = self.temp_icua

    def login(self, user="sudhir.j@gmail.com", admin=True):
        users.get_current_user = lambda user = user : users.User(user) if user else None
        if user == None: admin = False
        users.is_current_user_admin = lambda admin = admin : admin

    def logout(self):
        self.login(None)

    def make_test_data(self):
        self.evam = Company(name='Evam Theatre Company', url='evam')
        self.evam.put()
        self.chennai = City(name='Chennai', url='chennai')
        self.chennai.put()
