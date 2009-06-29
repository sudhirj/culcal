import datetime
from google.appengine.ext import db
import validators

# These mixins are only applicable to class derived from the base entity in base.py

class HasPerformances:
    def get_new_performances(self):
        return self.get_performances_from_time(datetime.datetime.now())
    
    def get_performances_from_time(self, dt):
        performance_query = self.cached_performances if hasattr(self, 'cached_performances') else  self.performances
        return performance_query.filter('utc_date_time >', dt).order('utc_date_time') 

class HasUrl:
    @classmethod
    def get_by_url(cls, url):
        return cls._get_attribute_by_value(cls.all(), 'url', url)