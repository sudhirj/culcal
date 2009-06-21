from google.appengine.api import users
from google.appengine.ext import db
from models.city import City
from models.company import Company
from models.show import Show
from models.venue import Venue
from models.performance import Performance
import unittest, datetime, random
from resources.webtest import TestApp
from handlers.public import main as public_main
from handlers.admin import main as admin_main
from resources.stubout import StubOutForTesting

class ExtendedTestCase(unittest.TestCase): 
    public_app = TestApp(public_main.createApp())
    admin_app = TestApp(admin_main.createApp())
    _login_stubs = StubOutForTesting()
    stubs = StubOutForTesting()
    
    def random(self):
        import hashlib, time
        return hashlib.md5((time.clock()*random.random()).__str__()).hexdigest()
    
    def setUp(self):
        self.make_test_data()
        self.login()
      
    def tearDown(self):
        self.logout()
        self.stubs.UnsetAll()
        for model in [City, Company, Performance, Show, Venue]:
            for datum in model.all():
                datum.delete()

    def login(self, user="sudhir.j@gmail.com", admin=True):
        self._login_stubs.Set(users, 'get_current_user', lambda user = user : users.User(user))
        self._login_stubs.Set(users, 'is_current_user_admin', lambda admin = admin : admin)

    def logout(self):
        self._login_stubs.UnsetAll()

    def make_test_data(self):
        now = datetime.datetime.now()
        self.now = datetime.datetime(year = now.date().year, month = now.date().month, day = now.date().day, hour = now.time().hour, minute = now.time().minute)
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

