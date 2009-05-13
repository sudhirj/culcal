from google.appengine.ext import db
import base

class Company(base.UrlBasedEntity):
    def get_show_by_url(self, show_url):
        matches = self.shows.filter('url =', show_url).fetch(1)
        return matches[0] if len(matches) else None
