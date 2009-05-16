import base

class Company(base.UrlBasedEntity):
    def get_show_by_url(self, show_url):
        return self._get_attribute_by_value(self.shows, 'url', show_url)
