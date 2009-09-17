import datetime
from google.appengine.ext import db
import validators
import helpers
from helpers.staticmap import StaticMapBuilder

# These mixins are only applicable to class derived from the base entity in base.py

class HasPerformances:
    
    def get_performances(self, start_after=None):
        from performance import Performance
        start_after = Performance.make_time_str(start_after or datetime.datetime.now())
        return self._performace_list.filter('time_sort >', start_after).order('time_sort')

    @property
    def _performace_list(self):
        return (self.cached_performances if hasattr(self, 'cached_performances') else  self.performances)
        
class HasUrl:
    @classmethod
    def get_by_url(cls, url):
        return cls._get_attribute_by_value(cls.all(), 'url', url)
        
class HasLocation:
    def get_map_url(self):
        return StaticMapBuilder().addMarker(self.location.lat, self.location.lon).build()
