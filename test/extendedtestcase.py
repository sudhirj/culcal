from google.appengine.api import users
from models.city import City
from models.company import Company
from models.show import Show
from models.venue import Venue
from models.performance import Performance
import unittest, datetime, random

class ExtendedTestCase(unittest.TestCase): 
    def random(self):
        import hashlib, time
        return hashlib.md5((time.clock()*random.random()).__str__()).hexdigest()
    
    def setUp(self):
        self.temp_gcu = users.get_current_user
        self.temp_icua = users.is_current_user_admin
        self.make_test_data()
      
    def tearDown(self):
        users.get_current_user = self.temp_gcu
        users.is_current_user_admin = self.temp_icua
        
        for model in [City, Company, Performance, Show, Venue]:
            for datum in model.all():
                datum.delete()

    def login(self, user="sudhir.j@gmail.com", admin=True):
        users.get_current_user = lambda user = user : users.User(user) if user else None
        if user == None: admin = False
        users.is_current_user_admin = lambda admin = admin : admin

    def logout(self):
        self.login(None)

    def make_test_data(self):
        self.now = datetime.datetime.now()
        self.one_day_later = self.now + datetime.timedelta(days=1)
        self.two_days_later = self.now + datetime.timedelta(days=2)
        self.three_days_later = self.now + datetime.timedelta(days=3)
        
        self.evam = Company(name='Evam Theatre Company', url='evam')
        self.evam.put()
        self.hamlet = Show(name='Hamlet', url='hamlet', company=self.evam)
        self.hamlet.put()
        self.chennai = City(name='Chennai', url='chennai')
        self.chennai.put()
        self.lady_andal = Venue(name='Lady Andal', url='lady_andal', city=self.chennai)
        self.lady_andal.put()
        
    def make_performance(self, show, venue, dt):
        perf = Performance(show=show, venue=venue, utc_date_time=dt)
        perf.put()
        return perf
