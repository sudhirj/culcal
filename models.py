from datetime import timedelta, tzinfo
from google.appengine.ext import db
import re
import settings
import validators

class Entity(db.Model):
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)
    
    @staticmethod
    def _get_attribute_by_value(attribute, filter_property, value):
        matches = attribute.filter(filter_property + ' =', value).fetch(1)
        return matches[0] if len(matches) else None

class HasPerformances:
    def get_performances(self, start_after=None):
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

        
class NamedEntity(Entity):
    def validate_name(string):
        if string == None or string.isspace() : raise ValueError("Name can't be blank")

    name = db.StringProperty(required=True, validator=validate_name)

    @property
    def str(self):
        return self.name.upper().strip().replace(' ','')
    
  
class UrlBasedEntity(NamedEntity, HasUrl):
    url = db.StringProperty(required=True, validator=validators.validate_url)
    def put(self):
        if (not self.is_saved()) and self.get_by_url(self.url):
            raise ValueError("This URL is already in use.")
        super(UrlBasedEntity, self).put()

    def get_route(self):
        return '/'+self.url

class FixedOffset(tzinfo):
    def __init__(self, offset):
        self.__offset = offset

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return "FixedOffset:" + self._offset 

    def dst(self, dt):
        return None
    
    def __eq__(self, other):
        return self.__offset == other.__offset
      
class City(base.UrlBasedEntity, HasPerformances):
    hours_offset = db.IntegerProperty(default=0)
    minutes_offset = db.IntegerProperty(default=0)

    def get_venue_by_url(self, venue_url):
        return self._get_attribute_by_value(self.venues, 'url', venue_url)

    def get_timedelta(self):
        return timedelta(hours=self.hours_offset, minutes=self.minutes_offset)

    def delete(self):
        for venue in self.venues: venue.delete()
        return super(City, self).delete()      

class Company(base.UrlBasedEntity, HasPerformances):
    description = db.TextProperty(required = False, default = "")

    def get_show_by_url(self, show_url):
        return self._get_attribute_by_value(self.shows, 'url', show_url)

    def put(self):
        if City.get_by_url(self.url): raise ValueError('This url is being used by a city')
        return super(Company, self).put()

    def delete(self):
        for show in self.shows: show.delete()
        return super(Company, self).delete()


class Performance(base.Entity):
    show = db.ReferenceProperty(Show, collection_name='performances', required=True)
    utc_date_time = db.DateTimeProperty(required=True)
    venue = db.ReferenceProperty(Venue, collection_name='performances', required=True)
    time_sort = db.StringProperty()

    cached_city = db.ReferenceProperty(City, collection_name = 'cached_performances', required = False)
    cached_company = db.ReferenceProperty(Company, collection_name = 'cached_performances', required = False)

    def get_local_time(self):
        return self.utc_date_time + self.venue.city.get_timedelta()

    def set_local_time(self, date_time):
        self.utc_date_time = date_time - self.venue.city.get_timedelta()

    def put(self):
        self.cached_city = self.venue.city
        self.cached_company = self.show.company
        self.time_sort = self.make_time_str(self.utc_date_time) + '|' + self.show.url + '|' +self.venue.url
        return super(Performance, self).put()

    def __eq__(self,other):
        if self.is_saved(): return self.key() == other.key()
        raise Error('Not Implemented')

    @staticmethod
    def make_time_str(dt):
        return dt.strftime('%Y-%m-%d|%H:%M|GMT') if hasattr(dt, "strftime") else dt

class Show(base.NamedEntity, HasPerformances, HasUrl):
    company = db.ReferenceProperty(Company,collection_name='shows', required = True)
    url = db.StringProperty(required = True, validator = validators.validate_url)
    description = db.TextProperty()

    def put(self):
        if (not self.is_saved()) and self.company.get_show_by_url(self.url):
            raise ValueError("This URL is being used for another show by "+self.company.name)
        super(Show, self).put()

    def get_route(self):
        return '/'+self.company.url+'/shows/'+self.url

    def delete(self):
        for performance in self.performances: performance.delete()
        return super(Show, self).delete()        
        

class Venue(base.NamedEntity, HasPerformances, HasUrl, HasLocation):
    city = db.ReferenceProperty(City, collection_name='venues')
    url = db.StringProperty(required=True, validator=validators.validate_url)
    location = db.GeoPtProperty()

    def put(self):
        if (not self.is_saved() and self.city.get_venue_by_url(self.url)):
            raise ValueError('This URL is already being used by another venue in ' + self.city.name)
        if not self.location: self.location = db.GeoPt(lat = 0, lon=0)
        super(Venue, self).put()

    def get_route(self):
        return '/'+self.city.url+'/venues/'+self.url

    def delete(self):
        for performance in self.performances: performance.delete()
        return super(Venue, self).delete()
        