import datetime
from google.appengine.ext import db
import validators
import helpers
from helpers.staticmap import StaticMapBuilder

# These mixins are only applicable to class derived from the base entity in base.py

class HasPerformances:
    def get_new_performances(self, start_after=None):
        if not start_after: return self.get_performances_from_time(datetime.datetime.now())
        return self._performace_list.filter('time_sort >', start_after)
    
    def get_performances_from_time(self, dt):
        return self._performace_list.filter('utc_date_time >', dt).order('utc_date_time') 

    @property
    def _performace_list(self):
        return self.cached_performances if hasattr(self, 'cached_performances') else  self.performances
        
class HasUrl:
    @classmethod
    def get_by_url(cls, url):
        return cls._get_attribute_by_value(cls.all(), 'url', url)
        
class HasLocation:
    def get_map_url(self):
        return StaticMapBuilder().addMarker(self.location.lat, self.location.lon).build()
